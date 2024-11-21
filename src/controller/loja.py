from controller.produto import ProdutoController
from controller.scrapper import ScrapperController
from controller.database import DatabaseController
import re
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class LojaController:
    def __init__(self, regexProduto=None, xpathProduto=None, xpathFiltro=None,xpathPesquisa=None,xpathBotaoPesquisa=None,xpathListaPesquisa=None):
        self.regexProduto = regexProduto
        self.xpathProduto = xpathProduto
        self.xpathFiltro = xpathFiltro
        self.xpathPesquisa = xpathPesquisa
        self.xpathBotaoPesquisa = xpathBotaoPesquisa
        self.xpathListaPesquisa = xpathListaPesquisa
        self.produtos = []

    
    def from_xpathProduto(cls, xpathProduto, xpathFiltro=None):
        return cls(xpathProduto=xpathProduto, xpathFiltro=xpathFiltro)

    def atualizaProdutos(self):
        for produto in self.produtos:
            produto.getPrice()
            
    def atualizaProdutosNoDB(self,url):
        for produto in self.produtos:
            produto.getPrice()

    def is_valid(item):
        return all(char.isalnum() or char.isspace() for char in item)


    def getFiltros(self, url):
        scrapper = ScrapperController(url, self.xpathFiltro)
        filtro = scrapper.get_element_value()
        if filtro == None:
            return None
        filtro = re.sub(r'\(.*?\)', '  ', filtro)
        filtro = filtro.split('  ')
        # filtro = filtro.replace('\n','')
        filtro = list(filter(None, filtro))
        filtro = [item.replace('\n', '') for item in filtro if any(char.isalpha() for char in item)]
        return filtro
    
    def addProduto(self, url):
        if(self.regexProduto != None):
            produto = ProdutoController(self.regexProduto, self.xpathProduto, url)
            self.produtos.append(produto)
        else:
            produto = ProdutoController(None, self.xpathProduto, url)
            self.produtos.append(produto)
        
        return produto
    
    def pesquisarProduto(self,url,pesquisa):
        scrapper = ScrapperController(url, xpathPesquisa=self.xpathPesquisa, xpathBotaoPesquisa=self.xpathBotaoPesquisa, xpathListaPesquisa=self.xpathListaPesquisa)
        data = scrapper.pesquisarProduto(pesquisa)
        if data['url']:
            links = scrapper.get_link(self.xpathListaPesquisa,data['url'])
        
            if links:
                for link in links:
                    self.addProduto(link)
                for produto in self.produtos:
                    produto.getPrice()
            return data
        
    