from model.produto import Produto
from src.view.menu_view.produto.descricao_produto import descricao_produto
from src.view.menu_view.produto.adicionar_produto import adicionar_produto
import os; 

def ver_produtos():
    while True:
        print("\n--- Ver monitoramentos ---")
        print("1. Adicionar monitoramento")
        print("2. Voltar ao menu principal")
        i = 3
        produtos = Produto().getProdutos()
        if(produtos == None):
            print("Nenhum monitoramento adicionado.")
        for produto in produtos:
            print(f"{i}. {produto[2]}")
            i+=1
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        elif  opcao.isdigit() and int(opcao) >= 3 and int(opcao) < i:
            descricao_produto(produtos[int(opcao)-3])
        else:
            print("Opção inválida. Tente novamente.")