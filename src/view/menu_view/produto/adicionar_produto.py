import re
import os; 
from controller.database import DatabaseController
from view.menu_view.loja.adicionar_loja import adicionar_loja
from view.menu_view.monitoracao.adicionar_monitoracao import adicionar_monitoracao

def adicionar_produto():
    database = DatabaseController()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Adicionar Monitoração")
    
    # Solicita o nome, validando a entrada para garantir que não seja deixado em branco
    while True:
        nome = input("Insira o nome: ").strip()
        if nome:
            break
        print("Insira um nome válido")
    
    # Solicita a URL, validando a entrada para garantir que não seja deixado em branco
    while True:
        url = input("Insira a URL: ").strip()
        if url:
            site = gerarNomeSite(url)
            break
        print("Insira uma URL válida")
        
    contagem = database.sqlRead(f"select count(*) from loja where site = '{site}';")
    
    contagem = contagem[0]['count'] if contagem else 0
    
    if contagem == 0:
        print("Não foi possível encontrar a loja associada a URL informada.")
        adicionar_loja()
        database.sqlWrite(f"INSERT INTO public.product (name, site, url) VALUES('{nome}', '{site}', '{url}');")
    else:
        database.sqlWrite(f"INSERT INTO public.product (name, site, url) VALUES('{nome}', '{site}', '{url}');")
    
    while True:
        monitoracao = input("Deseja adicionar monitoração(S/N): ").lower()
        if monitoracao == "s":
            adicionar_monitoracao(url)
            break
        elif monitoracao == "n":
            break
            
    
    
def gerarNomeSite(url):
    # Expressão regular para extrair o nome do site
    match = re.search(r'([a-zA-Z0-9-]+)(?=\.(com|org|net)|https:\/\/|www\.)', url)
    if match:
        nome_site = match.group(1).lower()  # Acessa o primeiro grupo e converte para minúsculas
        return nome_site
    return None