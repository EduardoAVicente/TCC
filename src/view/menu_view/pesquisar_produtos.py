from controller.pesquisarProdutos import PesquisarProdutos

def pesquisar_produtos():
    buscador = PesquisarProdutos('https://www.mercadolivre.com.br/', '//*[@id="cb1-edit"]','/html/body/header/div/div[2]/form/button')
    while True:
            pesquisa = input("Digite o nome do produto que deseja pesquisar: ")
            if pesquisa:
                buscador.pesquisarProduto(pesquisa)
            print("Insira um nome válido")
            