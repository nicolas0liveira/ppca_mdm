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

# Desabilita warnings de SSL (verify=False)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://www.gov.br/pgfn/pt-br/assuntos/divida-ativa-da-uniao/transparencia-fiscal-1/dados-abertos"
RETRY_LIMIT = 3
RETRY_DELAY = 5  # segundos entre as tentativas

# timestamp_run = datetime.now().strftime("%Y%m%d%H%M")
BASE_DOWNLOAD_DIR = f"downloads"
os.makedirs(BASE_DOWNLOAD_DIR, exist_ok=True)
LOG_PATH = os.path.join(BASE_DOWNLOAD_DIR, "download_log.csv")

downloaded_successfully = set()
errored_links = set()

RETRY_ERRORS_ONLY = "--retry-errors" in sys.argv

def get_links_from_page(url):
    print("🌐 Buscando links da página (com verificação de certificado desativada)...")
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
    filename = url.split("/")[-1]
    subfolder = extract_subfolder_from_url(url)
    save_dir = os.path.join(base_folder, subfolder) if subfolder else base_folder
    os.makedirs(save_dir, exist_ok=True)
    local_filename = os.path.join(save_dir, filename)

    if not RETRY_ERRORS_ONLY and url in downloaded_successfully:
        print(f"⏭️ Pulando (já baixado com sucesso): {filename}")
        return
    if RETRY_ERRORS_ONLY and url not in errored_links:
        return

    for attempt in range(1, RETRY_LIMIT + 1):
        try:
            print(f"⬇️ Baixando ({attempt}/{RETRY_LIMIT}): {filename}")
            response = requests.get(url, stream=True, verify=False, timeout=60)
            response.raise_for_status()
            total = int(response.headers.get('content-length', 0))

            with open(local_filename, 'wb') as file, tqdm(
                desc=filename,
                total=total,
                unit='B',
                unit_scale=True,
                unit_divisor=1024,
            ) as bar:
                for data in response.iter_content(chunk_size=1024):
                    size = file.write(data)
                    bar.update(size)

            print(f"✔️ Sucesso: {filename}")
            log_download(url, local_filename, filename, "success")
            return  # sucesso, sai do loop

        except Exception as e:
            print(f"⚠️ Tentativa {attempt} falhou: {e}")
            if attempt < RETRY_LIMIT:
                print(f"⏳ Aguardando {RETRY_DELAY}s para tentar novamente...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"❌ Falha definitiva ao baixar {filename}")
                log_download(url, local_filename, filename, "error")

if __name__ == "__main__":
    try:
        init_log()
        links = get_links_from_page(BASE_URL)
        print(f"{len(links)} arquivos encontrados.")
        for link in links:
            download_file(link, BASE_DOWNLOAD_DIR)
        print(f"\n📝 Log salvo em: {LOG_PATH}")
    except Exception as e:
        print(f"❌ Erro geral: {e}")
