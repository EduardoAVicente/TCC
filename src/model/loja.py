from controller.database import DatabaseController
from decimal import Decimal
import matplotlib.pyplot as plt
from datetime import datetime
import re
class Loja:
    def __init__(self):
        self.database = DatabaseController()

    def getLojas(self):
        return self.database.getData("loja")
    
    def xpathProdutoexist(self,url):
        return self.database.sqlRead(f"select count(*) from loja where url = {url} and xpathproduto is not null")
    

    def getRegex(self,LINK):
        LINK = self.gerarNomeSite(LINK)
        name = DatabaseController().sqlRead(f"Select regexproduto from loja where site = '{LINK}'")
        if name:
            return name[0]['regexproduto']
        else:
            return None 
        

    def getXpathProduto(self,LINK):
        LINK = self.gerarNomeSite(LINK)
        name = DatabaseController().sqlRead(f"Select xpathproduto from loja where site = '{LINK}'")
        if name:
            return name[0]['xpathproduto']
        else:
            return None 
        
    def getXpathFiltro(self,LINK):
        LINK = self.gerarNomeSite(LINK)
        name = DatabaseController().sqlRead(f"Select xpathfiltro from loja where site = '{LINK}'")
        if name:
            return name[0]['xpathfiltro']
        else:
            return None 
        
    def getXpathPesquisa(self,LINK):
        LINK = self.gerarNomeSite(LINK)
        name = DatabaseController().sqlRead(f"Select xpathpesquisa from loja where site = '{LINK}'")
        if name:
            return name[0]['xpathpesquisa']
        else:
            return None 
        
    def getXpathBotaoPesquisa(self,LINK):
        LINK = self.gerarNomeSite(LINK)
        name = DatabaseController().sqlRead(f"Select xpathbotaopesquisa from loja where site = '{LINK}'")
        if name:
            return name[0]['xpathbotaopesquisa']
        else:
            return None 
        
        
    def gerarNomeSite(self,url):
        # Expressão regular para extrair o nome do site
        match = re.search(r'([a-zA-Z0-9-]+)(?=\.(com|org|net)|https:\/\/|www\.)', url)
        if match:
            nome_site = match.group(1).lower()  # Acessa o primeiro grupo e converte para minúsculas
            return nome_site
        return None
    


  