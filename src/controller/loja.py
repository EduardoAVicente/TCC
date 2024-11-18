from controller.produto import ProdutoController
from controller.scrapper import ScrapperController
from controller.database import DatabaseController
import re
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


class LojaController:
    def __init__(self, regexProduto=None, xpathProduto=None, xpathFiltro=None,xpathPesquisa=None,xpathBotaoPesquisa=None,xpathListaPesquisa=None):
        self.regexProduto = regexProduto
        self.xpathProduto = xpathProduto
        self.xpathFiltro = xpathFiltro
        self.xpathPesquisa = xpathPesquisa
        self.xpathBotaoPesquisa = xpathBotaoPesquisa
        self.xpathListaPesquisa = xpathListaPesquisa
        self.produtos = []

    
    def from_xpathProduto(cls, xpathProduto, xpathFiltro=None):
        return cls(xpathProduto=xpathProduto, xpathFiltro=xpathFiltro)

    def atualizaProdutos(self):
        for produto in self.produtos:
            produto.getPrice()

    def is_valid(item):
        return all(char.isalnum() or char.isspace() for char in item)


    def getFiltros(self, url):
        scrapper = ScrapperController(url, self.xpathFiltro)
        filtro = scrapper.get_element_value()
        if filtro == None:
            return None
        filtro = re.sub(r'\(.*?\)', '  ', filtro)
        filtro = filtro.split('  ')
        # filtro = filtro.replace('\n','')
        filtro = list(filter(None, filtro))
        filtro = [item.replace('\n', '') for item in filtro if any(char.isalpha() for char in item)]
        return filtro
    
    def addProduto(self, url):
        if(self.regexProduto != None):
            produto = ProdutoController(self.regexProduto, self.xpathProduto, url)
            self.produtos.append(produto)
        else:
            produto = ProdutoController(None, self.xpathProduto, url)
            self.produtos.append(produto)
        
        return produto
    
    def pesquisarProduto(self, texto):
        max_attempts = 5  # Número máximo de tentativas
        attempt = 0

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            page.goto(url, wait_until="load")

            while attempt < max_attempts:
                try:
                    # Localiza a caixa de texto e tenta inserir o texto
                    element = page.locator(f'xpath={self.xpath}')
                    element.fill(texto)
                    print("Texto inserido com sucesso.")

                    # Se `self.xpathBotaoPesquisa` não for None, tenta localizar e clicar no botão
                    if self.xpathBotaoPesquisa:
                        botao_element = page.locator(f'xpath={self.xpathBotaoPesquisa}')
                        botao_element.click()
                        print("Botão pressionado com sucesso.")

                    # Tenta localizar o elemento da lista de pesquisa e imprimir o valor
                    lista_element = page.locator(f'xpath={self.xpathListaPesquisa}')
                    valor_lista = lista_element.inner_text()  # Obtém o texto do elemento
                    print(f"Valor encontrado: {valor_lista}")
                    
                    return  # Sai da função se tudo for bem-sucedido

                except Exception as e:
                    attempt += 1
                    print(f"Tentativa {attempt} falhou: {e}. Tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente

            print("Não foi possível realizar a operação após 5 tentativas.")
            browser.close()

                

 