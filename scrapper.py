from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

class Scrapper:
    def __init__(self, url, xpath):
        self.url = url
        self.xpath = xpath

    # Função para pegar o valor de um elemento a partir de uma URL e um XPath
    def get_element_value(self):
        # Configurando o WebDriver para rodar em modo headless (sem interface gráfica)
        options = Options()
        options.headless = False  # Definindo para True para rodar sem interface gráfica
        driver = webdriver.Firefox(options=options)

        try:
            # Navegar até a URL fornecida
            driver.get(self.url)
            driver.implicitly_wait(10)  # Espera implícita de 10 segundos

            # Encontrar o elemento usando o XPath fornecido
            element = driver.find_element(By.XPATH, self.xpath)

            # Retornar o valor (texto) do elemento encontrado
            return element.text
        except Exception as e:
            return str(e)
        finally:
            # Fechar o WebDriver
            driver.quit()
