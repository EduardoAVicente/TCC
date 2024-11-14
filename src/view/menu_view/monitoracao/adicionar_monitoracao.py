import os
from controller.database import DatabaseController
from datetime import datetime
import re

def adicionar_monitoracao(url):
    os.system('cls' if os.name == 'nt' else 'clear')
    if DatabaseController().sqlRead(f"select count(*) from loja where xpathproduto is not null and REGEXPRODUTO is not null and site = '{gerarNomeSite(url)}';")[0]['count'] == 0:
        print("Nenhum Xpath cadastrado para essa loja")
        print()
        return
    while True:
        print("Adicionar monitoração")

        minuto = input("Frequência(min): ")
        if minuto and minuto.isdigit() == False:
            print("Frequência inserida não é valida")
            print()
        else:
            DatabaseController().sqlWrite(f"INSERT INTO public.monitoria(url, minuto,date) VALUES ('{url}', {minuto}, TO_TIMESTAMP('{getDate()}', 'DD/MM/YYYY HH24:MI:SS'));")
            break
        
def getDate():
    now = datetime.now()
    formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
    return formatted_date

def gerarNomeSite(url):
    # Expressão regular para extrair o nome do site
    match = re.search(r'([a-zA-Z0-9-]+)(?=\.(com|org|net)|https:\/\/|www\.)', url)
    if match:
        nome_site = match.group(1).lower()  # Acessa o primeiro grupo e converte para minúsculas
        return nome_site
    return None