import tkinter as tk  # Importa a biblioteca tkinter para criar a interface gráfica
from tkinter import filedialog  # Importa o módulo filedialog do tkinter para lidar com caixas de diálogo de arquivo
import sys  # Importa o módulo sys para lidar com funções relacionadas ao sistema

def abrir_arquivo_e_processar():  # Define a função para abrir e processar o arquivo
    root = tk.Tk()  # Cria uma instância da janela principal do tkinter
    root.withdraw()  # Oculta a janela principal

    # Abre a caixa de diálogo para selecionar o arquivo de origem
    arquivo_path = filedialog.askopenfilename(title="Selecione o arquivo TXT", filetypes=[("Arquivos de texto", "*.txt")])
    if arquivo_path:  # Verifica se um arquivo foi selecionado
        processar_arquivo(arquivo_path)  # Chama a função para processar o arquivo selecionado

def processar_arquivo(arquivo_path):  # Define a função para processar o arquivo
    try:  # Inicia um bloco try-except para capturar possíveis erros
        with open(arquivo_path, 'r', encoding='utf-8') as arquivo:  # Abre o arquivo de origem em modo de leitura
            linhas = arquivo.readlines()  # Lê todas as linhas do arquivo e as armazena em uma lista

        novo_conteudo = ""  # Inicializa uma string vazia para armazenar o novo conteúdo do arquivo
        for linha in linhas:  # Itera sobre cada linha do arquivo
            if linha.strip():  # Verifica se a linha não está em branco
                partes = linha.split(' - ')  # Divide a linha em partes usando ' - ' como delimitador
                data_hora = partes[0]  # Obtém a data e hora da mensagem
                mensagem = ' - '.join(partes[1:])  # Obtém a mensagem excluindo a data e hora
                nova_linha = f"{data_hora}\n\n- {mensagem.strip().replace('.', '. ')}\n\n{'_'*30}\n\n"
                # Formata a nova linha com a data, mensagem formatada e separadores
                novo_conteudo += nova_linha  # Adiciona a nova linha ao conteúdo do arquivo modificado

        salvar_arquivo_modificado(novo_conteudo)  # Chama a função para salvar o arquivo modificado
    except Exception as e:  # Captura qualquer exceção que ocorra durante o processamento do arquivo
        tk.messagebox.showerror("Erro", f"Ocorreu um erro ao processar o arquivo: {str(e)}")
        # Exibe uma mensagem de erro com detalhes sobre a exceção ocorrida

def salvar_arquivo_modificado(novo_conteudo):  # Define a função para salvar o arquivo modificado
    root = tk.Tk()  # Cria uma instância da janela principal do tkinter
    root.withdraw()  # Oculta a janela principal

    # Abre a caixa de diálogo para salvar o arquivo modificado
    novo_arquivo_path = filedialog.asksaveasfilename(title="Salvar arquivo TXT modificado", defaultextension=".txt", filetypes=[("Arquivos de texto", "*.txt")])
    if novo_arquivo_path:  # Verifica se um local de salvamento foi escolhido
        with open(novo_arquivo_path, 'w', encoding='utf-8') as novo_arquivo:  # Abre o novo arquivo em modo de escrita
            novo_arquivo.write(novo_conteudo)  # Escreve o conteúdo modificado no novo arquivo
        tk.messagebox.showinfo("Sucesso", "Arquivo modificado salvo com sucesso.")
        # Exibe uma mensagem de sucesso após salvar o arquivo modificado

if __name__ == "__main__":  # Verifica se o script está sendo executado diretamente
    abrir_arquivo_e_processar()  # Chama a função para abrir e processar o arquivo
    sys.exit(0)  # Encerra a execução do programa após o processamento do arquivo
