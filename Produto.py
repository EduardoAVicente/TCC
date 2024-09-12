import re
from scrapper import Scrapper
from Database import Database

class Produto:
    def __init__(self, regex=None, xpath=None, url=None):
            self.regex = regex
            self.xpath = xpath
            self.url = url
            self.database = Database("motty.db.elephantsql.com", "5432", "vgdmtvyb", "vgdmtvyb", "qfwL0NkrP8m7jlrNd6fNdSu70n9Y3S0q")
            
            
    @classmethod
    def from_xpath(cls, xpath, url):
        return cls(url=url, xpath=xpath)
    
    def productExist(self):
        quantidade = self.database.sqlWrite(f"SELECT count(*) FROM PRODUCT where URL = '{self.url}'")
        # if(isinstance(quantidade, int, float)):
        #     if(quantidade == 0):
        #         return False
        #     else:
        #         return True
        # else:
        #     return False
        
        # Vai dar erro se a qunatidade for string?
        # return True if self.isNumber(quantidade) and quantidade != 0 else False
        if(self.isNumber(quantidade)):
            if(quantidade != 0):
                return True
        return False


    def getPrice(self):
        scrapper = Scrapper(self.url, self.xpath)
        price = scrapper.get_element_value().replace("\n", "").replace(",", ".")
        price = re.sub(r'\.(?=.*\.)', '', price)
        
                
        if(self.regex != None):
            # price = re.sub(repr(self.regex), "", price)
            price = re.sub(self.regex, "", price)
        
        print(price)
        print(not self.isNumber(price))
        if(not self.isNumber(price)):
            return None
        else:
            if self.productExist() == True:
                self.database.sqlWrite(f"INSERT INTO PRICE (URL,DATE,PRICE) VALUES ('{self.url}', CURRENT_DATE, '{price}')")
            else:
                # Adiconar porduto no database
                self.database.sqlWrite(f"INSERT INTO PRODUCT (URL, PRICE) VALUES ('{self.url}', '{price}')")
            return price
        
    def getPage(self):
        scrapper = Scrapper(self.url, self.xpath)
        return scrapper.getPage()
    
    def isNumber(self,numero):
        try:
            float(numero)  
            return True
        except ValueError:
            return False

    
    
