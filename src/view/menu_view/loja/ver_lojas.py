from model.loja import Loja
from view.menu_view.loja.descricao_loja import descricao_loja
from view.menu_view.loja.adicionar_loja import adicionar_loja
import os; 

def ver_lojas():
    while True:
        print("\n--- Ver monitoramentos ---")
        print("1. Adicionar loja")
        print("2. Voltar ao menu principal")
        i = 3
        lojas = Loja().getLojas()
        if(lojas == None):
            print("Nenhum monitoramento adicionado.")
        for loja in lojas:
            print(f"{i}. {loja[0]}")
            i+=1
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_loja()
        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif  opcao.isdigit() and int(opcao) >= 3 and int(opcao) < i:
            descricao_loja(lojas[int(opcao)-3])
        else:
            print("Opção inválida. Tente novamente.")