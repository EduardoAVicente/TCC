import re
# from Database import Database
from Produto import Produto

class loja:
    def __init__(self, regex=None, xpath=None):
            self.regex = regex
            self.xpath = xpath
            self.produtos = []
            # self.database = Database("motty.db.elephantsql.com", "5432", "vgdmtvyb", "vgdmtvyb", "qfwL0NkrP8m7jlrNd6fNdSu70n9Y3S0q")    

    @classmethod
    def from_xpath(cls, xpath):
        return cls(xpath=xpath)
        
    def addProduto(self, url):
        if(self.regex != ""):
            produto = Produto(self.regex,self.xpath,url)
            self.produtos.append(produto)
        else:
            produto = Produto("",self.xpath,url)
            self.produtos.append(produto)
        
        return produto
        

    def atualizaProdutos(self):
        for produto in self.produtos:
            print(produto.getPrice())
            
    
            