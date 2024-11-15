from src.view.menu_view.produto.ver_produtos import ver_produtos
from src.view.menu_view.loja.ver_lojas import ver_lojas
from src.view.menu_view.pesquisar_produtos import pesquisar_produtos
import os; 


class Menu:
    def main():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("########## Monitor de preços ##########")
            print("1. Ver monitoramentos")
            print("2. Pesquisar produtos")
            print("3. Ver lojas")
            print("0. Sair")
            
            opcao = input("Escolha uma opção: ")
            
            if opcao == "1":
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_produtos()
            elif opcao == "2":
                os.system('cls' if os.name == 'nt' else 'clear')
                pesquisar_produtos()
            elif opcao == "3":
                os.system('cls' if os.name == 'nt' else 'clear')
                ver_lojas()
            elif opcao == "0":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Tente novamente.")

    


