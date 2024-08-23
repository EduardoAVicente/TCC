import re
from scrapper import Scrapper

class Produto:
    def __init__(self, regex=None, xpath=None, url=None):
            self.regex = regex
            self.xpath = xpath
            self.url = url

    @classmethod
    def from_xpath(cls, xpath, url):
        return cls(url=url, xpath=xpath)

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
            return price
        
    def getPage(self):
        scrapper = Scrapper(self.url, self.xpath)
        return scrapper.getPage()