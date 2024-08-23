import re
from scrapper import Scrapper
from Produto import Produto

class loja:
    def __init__(self, regex=None, xpath=None):
            self.regex = regex
            self.xpath = xpath
            self.produtos = []

    @classmethod
    def from_xpath(cls, xpath):
        return cls(xpath=xpath)
        
    def addProduto(self, url):
        self.produtos.append(produto())
    
    def atualizaProdutos(self):
        for produto in self.produtos:
            produto.getPrice()

