import tkinter as tk
from tkinter import filedialog
import sys

# Função para abrir a caixa de diálogo e selecionar o arquivo TXT
def abrir_arquivo():
    root = tk.Tk()
    root.withdraw()
    arquivo_path = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Arquivos de texto", "*.txt")])
    if arquivo_path:
        processar_arquivo(arquivo_path)

# Função para processar o arquivo e realizar as modificações
def processar_arquivo(arquivo_path):
    with open(arquivo_path, 'r', encoding='utf-8') as arquivo:
        linhas = arquivo.readlines()

    novo_conteudo = ""
    for linha in linhas:
        # Verifica se a linha não está em branco
        if linha.strip():
            # Separar cada final de frase e adicionar espaço entre as datas
            partes = linha.split(' - ')
            data_hora = partes[0]
            mensagem = ' - '.join(partes[1:])
            # Adicionar espaço após o ponto final
            nova_linha = f"{data_hora} - {mensagem.strip().replace('.', '. ')}\n"
            novo_conteudo += nova_linha

    # Abrir a caixa de diálogo para salvar o novo arquivo TXT
    root = tk.Tk()
    root.withdraw()
    novo_arquivo_path = filedialog.asksaveasfilename(title="Salvar arquivo TXT modificado", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    if novo_arquivo_path:
        with open(novo_arquivo_path, 'w', encoding='utf-8') as novo_arquivo:
            novo_arquivo.write(novo_conteudo)

# Verificar se o código está sendo executado diretamente
if __name__ == "__main__":
    abrir_arquivo()
    # Encerrar o aplicativo após a execução
    sys.exit(0)
