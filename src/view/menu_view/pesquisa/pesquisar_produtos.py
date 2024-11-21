from controller.database import DatabaseController
from view.menu_view.pesquisa.resultado_pesquisa import resultado_pesquisa

def pesquisar_produtos():
    # Obtém as lojas disponíveis para pesquisa no banco de dados
    lojasBusca = DatabaseController().sqlRead(
        "SELECT regexproduto,site, URL,xpathproduto,xpathpesquisa, xpathbotaopesquisa, xpathfiltro,xpathlistapesquisa FROM loja WHERE URL IS NOT NULL AND xpathproduto IS NOT NULL AND regexproduto IS NOT NULL AND xpathpesquisa IS NOT NULL AND xpathlistapesquisa IS NOT NULL AND xpathbotaopesquisa IS NOT NULL;"
    )
    
    if not lojasBusca:  # Verifica se não há lojas cadastradas
        print("Não há lojas cadastradas para pesquisa")
        return

    while True:
        pesquisa = input("Digite o nome do produto que deseja pesquisar: ").strip()
        if pesquisa:  # Se o nome do produto for válido
            print("Selecione as lojas que deseja pesquisar:")
            for idx, loja in enumerate(lojasBusca, start=1):  # Enumera as lojas com índices começando em 1
                print(f"{idx} - {loja['site']}")

            lojasSelecionadas = input("Digite o número das lojas que deseja pesquisar, separados por espaços: ").strip()
            
            # Remove espaços, verifica se a entrada é válida e converte para inteiros
            if lojasSelecionadas.replace(" ", "").isdigit():
                lojasSelecionadas = [int(num) for num in lojasSelecionadas.split()]
                
                # Valida os números das lojas selecionadas
                if all(0 < loja <= len(lojasBusca) for loja in lojasSelecionadas):
                    lojasSelecionadas = [lojasBusca[loja-1] for loja in lojasSelecionadas]  # Obtém as lojas selecionadas
                    resultado_pesquisa(lojasSelecionadas,pesquisa)
                    
                  
                    break  # Sai do loop após a pesquisa
                else:
                    print("Erro: Alguns números inseridos estão fora do intervalo válido.")
            else:
                print("Erro: Entrada inválida. Digite apenas números separados por espaços.")
        else:
            print("Erro: Insira um nome de produto válido.")
