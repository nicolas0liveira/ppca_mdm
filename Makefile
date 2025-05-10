# Nome do script Python
SCRIPT_JUNTA_ARQUIVOS = utils/junta_arquivos.py
BASE_OUTPUT_DIR = output
PYTHON = python

.PHONY: run junta_arquivos setup clean help

help:
	@echo "Comandos disponíveis:"
	@echo "  make setup              # Instala dependências"
	@echo "  make junta_arquivos     # Executa o script de junção dos arquivos"
	@echo "  make run LOG=1          # Executa e salva caminho de saída em 'last_output_path.log'"
	@echo "  make clean              # Remove dados de saída"

# Instala as dependências necessárias
setup:
	@echo "📦 Instalando dependências (pandas, pyarrow)..."
	pip install -r requirements.txt

# Limpa todos os arquivos de saída
clean:
	@echo "🧹 Limpando diretórios de saída..."
	rm -rf $(BASE_OUTPUT_DIR)/*
	rm -f last_output_path.log

# Regra principal (pode ser genérica)
run: junta_arquivos

# Tarefa específica: junta arquivos em streaming
junta_arquivos:
	@echo "🚀 Executando script de junção de arquivos..."
	@$(PYTHON) $(SCRIPT_JUNTA_ARQUIVOS)
	@if [ "$(LOG)" = "1" ]; then \
		echo "📝 Salvando caminho de saída no log..."; \
		ls -td $(BASE_OUTPUT_DIR)/*_resultado_final | head -n1 > last_output_path.log; \
		echo "✅ Caminho salvo em last_output_path.log"; \
	fi
