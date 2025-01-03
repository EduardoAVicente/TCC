from controller.database import DatabaseController
from controller.scrapper import ScrapperController
from model.produto import Produto
from datetime import datetime
import re

class ProdutoController:
    def __init__(self, regex, xpath, url):
        self.regex = regex
        self.xpath = xpath
        self.url = url
        self.database = DatabaseController()

    def productExist(self):
        quantidade = self.database.sqlWrite(f"SELECT count(*) FROM PRODUCT where URL = '{self.url}'")
        quantidade = quantidade[0][0]

        if(self.isNumber(quantidade)):
            if(quantidade != 0):
                return True
        return False

    def getPrice(self):
        scrapper = ScrapperController(self.url, self.xpath)

        price = scrapper.get_element_value()
        if price:
            if(self.regex != None):
                
                # print("Preço(String bruta): " + price)
                price = price.replace("\n", "").replace(",", ".")
                price = re.sub(r'\.(?=.*\.)', '', price)
                price = re.sub(self.regex, "", price)
            else:
                # print("Tratamento regex não realizado: " + price)
                pass
            
            if(not self.isNumber(price)):
                # print("Preço(entrada invalida): " + price)
                return None
            else:
                if self.productExist() == True:
                    self.database.sqlWrite(f"INSERT INTO PRICE (URL, DATE, PRICE) VALUES ('{self.url}', TO_TIMESTAMP('{self.getDate()}', 'DD/MM/YYYY HH24:MI:SS'), {price});")

                else:
                    # Adiconar porduto no database
                    truncated_url = (self.url[:30] + '...') if len(self.url) > 30 else self.url
                    print(f"Produto {truncated_url} adicionado ao banco de dados com o preço {price} do site {self.gerarNomeSite(self.url)}\n\n")
                    self.database.sqlWrite(f"INSERT INTO PRODUCT (URL, name, site) VALUES ('{self.url}', '{Produto().getName(self.url)}', '{self.gerarNomeSite(self.url)}');")
                    self.database.sqlWrite(f"INSERT INTO PRICE (URL, DATE, PRICE) VALUES ('{self.url}', TO_TIMESTAMP('{self.getDate()}', 'DD/MM/YYYY HH24:MI:SS'), {price});")
                    # print("Produto adicionado ao banco de dados")
                # print("Preço: " + price)
                return price
        else:
            return None
    
    def getPage(self):
        scrapper = ScrapperController(self.url, self.xpath)
        return scrapper.getPage()
    
    def isNumber(self, numero):
        if numero is None:
            return False
        
        try:
            float(numero)
            return True
        except (ValueError, TypeError):
            return False

    def getDate(self):
        now = datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
        return formatted_date
    

    def gerarNomeSite(self,url):
        # Expressão regular para extrair o nome do site
        match = re.search(r'([a-zA-Z0-9-]+)(?=\.(com|org|net)|https:\/\/|www\.)', url)
        if match:
            nome_site = match.group(1).lower()  # Acessa o primeiro grupo e converte para minúsculas
            return nome_site
        return None