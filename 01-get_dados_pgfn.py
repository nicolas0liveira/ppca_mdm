import os
import csv
import requests
import sys
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from tqdm import tqdm
import urllib3
from datetime import datetime
import time
import re

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://www.gov.br/pgfn/pt-br/assuntos/divida-ativa-da-uniao/transparencia-fiscal-1/dados-abertos"
RETRY_LIMIT = 3
RETRY_DELAY = 5  # seconds

BASE_DOWNLOAD_DIR = "downloads"
os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)
LOG_PATH = os.path.join(BASE_DOWNLOAD_DIR, "download_log.csv")
UNIQUE_CSV_PATH = os.path.join(BASE_DOWNLOAD_DIR, "unique_downloads.csv")

downloaded_successfully = set()
errored_links = set()
final_filenames = dict()

RETRY_ERRORS_ONLY = "--retry-errors" in sys.argv

def get_links_from_page(url):
    print("🌐 Fetching links from page (SSL verification disabled)...")
    response = requests.get(url, verify=False)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    links = []
    for a in soup.find_all("a", href=True):
        href = a['href']
        if href.lower().endswith((".zip", ".csv", ".xls", ".xlsx", ".json")):
            full_url = urljoin(BASE_URL, href)
            links.append(full_url)
    return links

def extract_subfolder_from_url(url):
    path_parts = urlparse(url).path.strip("/").split("/")
    if len(path_parts) >= 2:
        return path_parts[-2]
    return None

def parse_year_quarter(folder_name):
    match = re.match(r"(\d{4})_trimestre_(\d{2})", folder_name)
    if match:
        year, quarter = match.groups()
        return f"{year}T{int(quarter)}"
    return None

def log_download(url, path, filename, status):
    with open(LOG_PATH, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([url, path, filename, datetime.now().isoformat(), status])

def init_log():
    if not os.path.exists(LOG_PATH):
        with open(LOG_PATH, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["url", "path", "filename", "timestamp", "status"])
    else:
        with open(LOG_PATH, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["status"] == "success":
                    downloaded_successfully.add(row["url"])
                elif row["status"] == "error":
                    errored_links.add(row["url"])

def download_file(url, base_folder):
    original_filename = url.split("/")[-1]
    subfolder = extract_subfolder_from_url(url)
    prefix = parse_year_quarter(subfolder) if subfolder else None

    if prefix:
        renamed_filename = f"{prefix}_{original_filename}"
        save_dir = base_folder
    else:
        renamed_filename = original_filename
        save_dir = os.path.join(base_folder, subfolder or "unknown")
        os.makedirs(save_dir, exist_ok=True)

    local_filename = os.path.join(save_dir, renamed_filename)

    if not RETRY_ERRORS_ONLY and url in downloaded_successfully:
        print(f"⏭️ Skipping (already downloaded): {renamed_filename}")
        return
    if RETRY_ERRORS_ONLY and url not in errored_links:
        return

    for attempt in range(1, RETRY_LIMIT + 1):
        try:
            print(f"⬇️ Downloading ({attempt}/{RETRY_LIMIT}): {renamed_filename}")
            response = requests.get(url, stream=True, verify=False, timeout=60)
            response.raise_for_status()
            total = int(response.headers.get('content-length', 0))

            with open(local_filename, 'wb') as file, tqdm(
                desc=renamed_filename,
                total=total,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in response.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)

            print(f"✔️ Success: {renamed_filename}")
            log_download(url, local_filename, renamed_filename, "success")
            final_filenames[url] = renamed_filename
            return

        except Exception as e:
            print(f"⚠️ Attempt {attempt} failed: {e}")
            if attempt < RETRY_LIMIT:
                print(f"⏳ Waiting {RETRY_DELAY}s before retrying...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"❌ Failed to download: {renamed_filename}")
                log_download(url, local_filename, renamed_filename, "error")

def write_unique_csv(mapping, csv_path):
    print(f"🧾 Writing unique download list to {csv_path}")
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "url"])
        for url, filename in sorted(mapping.items()):
            writer.writerow([filename, url])

if __name__ == "__main__":
    try:
        init_log()
        links = get_links_from_page(BASE_URL)
        print(f"{len(links)} files found.")
        for link in links:
            download_file(link, BASE_DOWNLOAD_DIR)
        write_unique_csv(final_filenames, UNIQUE_CSV_PATH)
        print(f"\n📝 Log saved at: {LOG_PATH}")
        print(f"📄 Unique download list saved at: {UNIQUE_CSV_PATH}")
    except Exception as e:
        print(f"❌ General error: {e}")
