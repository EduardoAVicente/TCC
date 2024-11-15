from controller.scrapper import ScrapperController

class PesquisarProdutos:
    def __init__(self,url,xpath,botao):
        self.scrapper = ScrapperController(url,xpath,botao)
        
    def pesquisarProduto(self,nome):
        self.scrapper.inserirDados(nome)