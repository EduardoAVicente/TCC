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
        if(self.database.sqlWrite("SELECT count(*) FROM PRODUCT") > 0):
            return True
        else:
            return False

    def getPrice(self):
        scrapper = Scrapper(self.url, self.xpath)
        price = scrapper.get_element_value().replace("\n", "").replace(",", ".")
        price = re.sub(r'\.(?=.*\.)', '', price)
                
        if(self.regex != None):
            # price = re.sub(repr(self.regex), "", price)
            price = re.sub(self.regex, "", price)
        
        if(price.replace(" ","") == "" or price == None):
            return None
        else:
            if productExist() == True:
                self.database.sqlWrite(f"INSERT INTO PRODUCT (URL, PRICE) VALUES ('{self.url}', '{price}')")
            else:
                No
            return price
        
    def getPage(self):
        scrapper = Scrapper(self.url, self.xpath)
        return scrapper.getPage()
    
    
