import re
from scrapper import Scrapper

class loja:
    def __init__(self, regex=None, xpath=None):
            self.regex = regex
            self.xpath = xpath

    @classmethod
    def from_xpath(cls, xpath):
        return cls(xpath=xpath)
        

    def getPrice(self, url):
        scrapper = Scrapper(url, self.xpath)
        price = scrapper.get_element_value().replace("\n", "").replace(",", ".")
        
        if(self.regex != None):
            price = re.sub(repr(self.regex), "", price)
        
        if(price.replace(" ","") == "" or price == None):
            return None
        else:
            return price
        
    def getPage(self, url):
        scrapper = Scrapper(url, self.xpath)
        return scrapper.getPage()
        
