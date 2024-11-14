import re
import os; 
from controller.database import DatabaseController

def adicionar_loja():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        site = input("Digite a url do site (obrigatório): ")
        if not site:
            print("O campo 'SITE' é obrigatório. Dados não inseridos.")
        elif not validar_url(site):
            print("Os dados inseridos não são uma URL válida.")
        else:
            break
        
    regex_produto = input("Digite o REGEXPRODUTO (opcional): ") or "Null"
    xpath_produto = input("Digite o XPATHPRODUTO (opcional): ") or "Null"
    xpath_filtro = input("Digite o XPATHFILTRO (opcional): ") or "Null"
    xpath_pesquisa = input("Digite o XPATHPESQUISA (opcional): ") or "Null"
    xpath_botao_pesquisa = input("Digite o XPATHBOTAOPESQUISA (opcional): ") or "Null"

    DatabaseController().sqlWrite(f"INSERT INTO public.loja (site, regexproduto, xpathproduto, xpathfiltro, xpathpesquisa, xpathbotaopesquisa) VALUES('{gerarNomeSite(site)}', '{regex_produto}', '{xpath_produto}', '{xpath_filtro}', '{xpath_pesquisa}', '{xpath_botao_pesquisa}');")

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