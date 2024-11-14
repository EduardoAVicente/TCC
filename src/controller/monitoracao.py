from datetime import datetime, timedelta
from controller.loja import LojaController
from controller.database import DatabaseController
import re

class MonitoracaoController():
    
    def __init__(self):
        self.database = DatabaseController()

    def main(self):
        while True:
            monitoria = self.database.getData("MONITORIA")
            
            for monitor in monitoria:
                url = monitor[0]
                data = monitor[1]
                minuto = monitor[2]
                
                dataLoja = self.database.sqlRead(f"SELECT regexproduto, xpathproduto FROM loja WHERE site = '{self.gerarNomeSite(url)}';")
                            
                regex = dataLoja[0]['regexproduto']
                xpathProduto = dataLoja[0]['xpathproduto']
                print(f"Site: {self.gerarNomeSite(url)} - Data: {data} - Minuto: {minuto} - Aprovado: {(data + timedelta(minutes=minuto)) <= datetime.now()}")        
                
                
                
                if (data + timedelta(minutes=minuto)) <= datetime.now():
                    loja = LojaController(regex, xpathProduto)
                    loja.addProduto(url)     
                    loja.atualizaProdutos()
                    
                    self.database.sqlWrite(f"UPDATE monitoria SET date = TO_TIMESTAMP('{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}', 'DD/MM/YYYY HH24:MI:SS') where url='{url}' and minuto = {minuto};")
            
        
        
    def gerarNomeSite(self,url):
        # Expressão regular para extrair o nome do site
        match = re.search(r'([a-zA-Z0-9-]+)(?=\.(com|org|net)|https:\/\/|www\.)', url)
        if match:
            nome_site = match.group(1).lower()  # Acessa o primeiro grupo e converte para minúsculas
            return nome_site
        return None