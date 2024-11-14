import os
from controller.database import DatabaseController
from datetime import datetime


def adicionar_monitoracao(url):
    os.system('cls' if os.name == 'nt' else 'clear')
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