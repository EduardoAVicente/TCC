from controller.database import DatabaseController
from decimal import Decimal
import matplotlib.pyplot as plt
from datetime import datetime

class Produto:
    def __init__(self):
        self.database = DatabaseController()

    
    def getProdutos(self):
        return self.database.getData("product")
    
    def getPrices(self, URL):
        # Chama sqlRead para obter os resultados brutos
        result = self.database.sqlRead(f"select price,date from price where url = '{URL}'")
        
        if result:
            formatted_results = []
            for item in result:
                formatted_item = {}
                for key, value in item.items():
                    if isinstance(value, Decimal):
                        # Formatar o Decimal (price)
                        formatted_item[key] = f"{value:.2f}"
                    elif isinstance(value, datetime):
                        # Formatar o datetime (date)
                        formatted_item[key] = value.strftime("%d/%m/%Y %H:%M")
                    else:
                        formatted_item[key] = value
                formatted_results.append(formatted_item)
            return formatted_results
        else:
            return None


    def gerarGraficoPreco(self, produto):
        # Verificação para produto vazio ou nulo
        if not produto or len(produto) < 3:
            return

        # Obtém os dados de preço usando o atributo URL do produto
        data = self.getPrices(produto[1])
        
        # Verificação se `data` é None
        if data is None:
            return

        datas = []
        precos = []
        
        # Preencher as listas com os valores de data e preço
        for item in data:
            # Convertendo a string de data para um objeto datetime
            data_obj = datetime.strptime(item['date'], "%d/%m/%Y %H:%M")
            datas.append(data_obj)
            precos.append(float(item['price']))  # Convertendo o preço para float
        
        # Criando o gráfico de linha
        plt.figure(figsize=(10, 6))
        plt.plot(datas, precos, marker='o', linestyle='-', color='b')
        
        # Adicionando título e rótulos
        plt.title(f"Histórico de preços do {produto[2]}")
        plt.xlabel("Data")
        plt.ylabel("Preço")
        
        # Melhorando a formatação do eixo X
        plt.xticks(rotation=45)  # Rotacionar as datas no eixo X para melhor visualização
        plt.tight_layout()  # Ajusta a exibição para não cortar os rótulos
        
        # Exibindo o gráfico
        plt.show()