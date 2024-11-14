import re
import os; 
from controller.database import DatabaseController

def adicionar_loja():
    os.system('cls' if os.name == 'nt' else 'clear')

from controller.database import DatabaseController
import os; 
os.system('cls' if os.name == 'nt' else 'clear')

def editar_loja(loja):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    regex_produto = input(f"Regex do produto[{loja[1]}]: ") or loja[1]
    xpathProduto = input(f"Xpath do produto[{loja[2]}]: ") or loja[2]
    xpathFiltro = input(f"Xpath dos filtros[{loja[3]}]: ") or loja[3]
    xpathBarraPesquisa = input(f"Xpath da barra de pesquisa[{loja[4]}]: ") or loja[4]
    xpathBotaoPesquisar = input(f"Xpath do botao de pesquisar[{loja[5]}]: ") or loja[5]

    site = loja[0]
    DatabaseController().sqlWrite(f"UPDATE public.loja SET regexproduto='{regex_produto}', xpathproduto='{xpathProduto}', xpathfiltro='{xpathFiltro}', xpathpesquisa='{xpathBarraPesquisa}', xpathbotaopesquisa='{xpathBotaoPesquisar}' WHERE site='{site}';")

def validar_url(url):
    pattern = re.compile(
        r'^(https?://)?'               # Protocolo opcional (http ou https)
        r'((([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})|'  # Domínio
        r'localhost|'                  # Localhost
        r'(\d{1,3}\.){3}\d{1,3})'      # Endereço IP
        r'(:\d+)?'                     # Porta opcional
        r'(/[\w\-./?%&=]*)?$'          # Caminho opcional
    )
    return bool(pattern.match(url))

def gerarNomeSite(url):
    # Expressão regular para extrair o nome do site
    match = re.search(r'([a-zA-Z0-9-]+)(?=\.(com|org|net)|https:\/\/|www\.)', url)
    if match:
        nome_site = match.group(1).lower()  # Acessa o primeiro grupo e converte para minúsculas
        return nome_site
    return None