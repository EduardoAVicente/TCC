from controller.database import DatabaseController
from view.menu_view.monitoracao.ver_monitoracao import ver_monitoracao
from view.menu_view.monitoracao.adicionar_monitoracao import adicionar_monitoracao
import os; 

def descricao_produto(produto):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(f"Nome: {produto[2]}")
    print(f"Site: {produto[0]}")
    print(f"URL: {produto[1]}")
    
    ver_monitoracao(produto)
    
    
    
    


    while True:
        deletar = input("Deseja deletar este item(S/N): ").lower()
        if deletar == "s":
            DatabaseController().sqlWrite(f"DELETE FROM public.product WHERE site='{produto[0]}';")
            break
        elif deletar == "n":
            while True:
                editar = input("Deseja adicionar monitoria nese item(S/N): ").lower()
                if editar == "s":
                    adicionar_monitoracao(produto[1])
                    break
                elif editar == "n":
                    break
            break
    