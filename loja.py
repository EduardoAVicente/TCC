import re
# from Database import Database
from Produto import Produto
from scrapper import Scrapper

class loja:
    def __init__(self, regex=None, xpathProduto=None, xpathFiltro=None):
        self.regex = regex
        self.xpathProduto = xpathProduto
        self.xpathFiltro = xpathFiltro
        self.produtos = []
        # self.database = Database("motty.db.elephantsql.com", "5432", "vgdmtvyb", "vgdmtvyb", "qfwL0NkrP8m7jlrNd6fNdSu70n9Y3S0q")    

    @classmethod
    def from_xpathProduto(cls, xpathProduto, xpathFiltro=None):
        return cls(xpathProduto=xpathProduto, xpathFiltro=xpathFiltro)

    def addProduto(self, url):
        if(self.regex != None):
            produto = Produto(self.regex, self.xpathProduto, url)
            self.produtos.append(produto)
        else:
            produto = Produto(None, self.xpathProduto, url)
            self.produtos.append(produto)
        
        return produto
        

    def atualizaProdutos(self):
        for produto in self.produtos:
            produto.getPrice()

    def is_valid(item):
        return all(char.isalnum() or char.isspace() for char in item)

    def getFiltros(self, url):
        scrapper = Scrapper(url, self.xpathFiltro)
        filtro = scrapper.get_element_value()
        filtro = filtro.replace('\n','')
        filtro = filtro.split('  ')
        filtro = list(filter(None, filtro))
        filtro = [item for item in filtro if any(char.isalpha() for char in item)] # n sei se ta funcionando
        return filtro