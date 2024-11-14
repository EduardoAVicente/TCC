import os;
from view.menu_view.loja.editar_loja import editar_loja 
from controller.database import DatabaseController
os.system('cls' if os.name == 'nt' else 'clear')

def descricao_loja(loja):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print(f"Site: {loja[0]}")
    print(f"Regex do produto: {loja[1]}")
    print(f"Xpath do produto: {loja[2]}")
    print(f"Xpath dos filtros: {loja[3]}")
    print(f"Xpath da barra de pesquisa: {loja[4]}")
    print(f"Xpath do botao de pesquisar: {loja[5]}")
    
    while True:
        editar = input("Deseja editar este item(S/N): ").lower()
        if editar == "s":
            editar_loja(loja)
            break
        elif editar == "n":
            while True:
                deletar = input("Deseja deletar este item(S/N): ").lower()
                if deletar == "s":
                    DatabaseController().sqlWrite(f"DELETE FROM public.loja WHERE site='{loja[0]}';")
                    break
                elif deletar == "n":
                    break
            break