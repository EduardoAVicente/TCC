from controller.database import DatabaseController
from decimal import Decimal
import matplotlib.pyplot as plt
from datetime import datetime

class Loja:
    def __init__(self):
        self.database = DatabaseController()

    def getLojas(self):
        return self.database.getData("loja")
    
    def xpathProdutoexist(self,url):
        return self.database.sqlRead(f"select count(*) from loja where url = {url} and xpathproduto is not null")
    
    


  