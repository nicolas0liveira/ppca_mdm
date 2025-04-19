import os
import subprocess
import sys

REQUIREMENTS = [
    "requests",
    "beautifulsoup4",
    "tqdm"
]

SCRIPT_NAME = "01-get_dados_pgfn.py"
VENV_PATH = "venv"
VENV_PYTHON = os.path.join(VENV_PATH, "bin", "python")
VENV_PIP = os.path.join(VENV_PATH, "bin", "pip")

def create_requirements_file():
    print("📦 Criando requirements.txt...")
    with open("requirements.txt", "w") as f:
        f.write("\n".join(REQUIREMENTS))
    print("✅ requirements.txt criado.")

def create_virtualenv():
    print("🛠️ Criando ambiente virtual em './venv'...")
    subprocess.check_call([sys.executable, "-m", "venv", VENV_PATH])
    print("✅ Ambiente virtual criado.")

def install_dependencies():
    print("📥 Instalando dependências dentro do ambiente virtual...")
    subprocess.check_call([VENV_PIP, "install", "-r", "requirements.txt"])
    print("✅ Dependências instaladas.")

def run_script_in_venv(script_name):
    print(f"\n🚀 Executando '{script_name}' com o Python da venv...\n")
    subprocess.check_call([VENV_PYTHON, script_name])

if __name__ == "__main__":
    create_requirements_file()

    if os.path.exists(VENV_PATH):
        print("🔄 Ambiente virtual já existe. Pulando criação e instalação.")
    else:
        create_virtualenv()
        install_dependencies()

    print("\n🎉 Setup concluído!")
    print("ℹ️ Para ativar manualmente o ambiente virtual: source venv/bin/activate")

    if os.path.exists(SCRIPT_NAME):
        opcao = input(f"\n❓ Deseja executar agora o script '{SCRIPT_NAME}' dentro da venv? (y/n): ").strip().lower()
        if opcao == "y":
            run_script_in_venv(SCRIPT_NAME)
    else:
        print(f"\n⚠️ Script '{SCRIPT_NAME}' não encontrado.")
