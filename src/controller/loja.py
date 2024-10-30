from controller.produto import ProdutoController
from controller.scrapper import ScrapperController
import re
class LojaController:
    def __init__(self, regex=None, xpathProduto=None, xpathFiltro=None):
        self.regex = regex
        self.xpathProduto = xpathProduto
        self.xpathFiltro = xpathFiltro
        self.produtos = []

    
    def from_xpathProduto(cls, xpathProduto, xpathFiltro=None):
        return cls(xpathProduto=xpathProduto, xpathFiltro=xpathFiltro)

    def atualizaProdutos(self):
        for produto in self.produtos:
            produto.getPrice()

    def is_valid(item):
        return all(char.isalnum() or char.isspace() for char in item)

    def getFiltros(self, url):
        scrapper = ScrapperController(url, self.xpathFiltro)
        filtro = scrapper.get_element_value()
        filtro = re.sub(r'\(.*?\)', '  ', filtro)
        filtro = filtro.split('  ')
        # filtro = filtro.replace('\n','')
        filtro = list(filter(None, filtro))
        filtro = [item.replace('\n', '') for item in filtro if any(char.isalpha() for char in item)]
        return filtro
    
    def addProduto(self, url):
        if(self.regex != None):
            produto = ProdutoController(self.regex, self.xpathProduto, url)
            self.produtos.append(produto)
        else:
            produto = ProdutoController(None, self.xpathProduto, url)
            self.produtos.append(produto)
        
        return produto