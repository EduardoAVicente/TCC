from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time
import re
from collections import defaultdict


class ScrapperController:
    def __init__(self, url=None, xpath=None,filtro=None,xpathPesquisa=None ,botao=None, xpathBotaoPesquisa=None,xpathListaPesquisa=None):
        self.url = url
        self.xpath = xpath
        self.botao = botao
        self.xpathPesquisa = xpathPesquisa
        self.xpathBotaoPesquisa = xpathBotaoPesquisa
        self.xpathListaPesquisa = xpathListaPesquisa
        self.filtro = filtro
        self.headless = False
        
        
    def getXpath(self, xpath):

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()

            try:
                # Acessa a URL e espera carregar
                page.goto(self.url, wait_until="load")
                
                # Localiza o elemento pelo XPath
                element = page.locator(f'xpath={xpath}').first
                
                # Retorna o texto do elemento
                return element.text_content(timeout=50000)
            except PlaywrightTimeoutError:
                print("Erro de timeout ao carregar a página.")
                return None
            except Exception as e:
                print(f"Erro inesperado: {e}")
                return None
            finally:
                browser.close()

    def get_element_value(self):
        max_attempts = 1  # Número máximo de tentativas
        attempt = 0

        with sync_playwright() as p:
            # Inicia o navegador
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()

            while attempt < max_attempts:
                try:
                    # Tenta carregar a página e espera até que ela esteja totalmente carregada
                    page.goto(self.url, wait_until="load")
                    
                    if self.xpath:
                        # Tenta localizar o elemento
                        element = page.locator(f'xpath={self.xpath}').first
                        # Aguarda até que o conteúdo do texto seja acessível
                        text_content = element.text_content(timeout=5000)
                        if text_content:
                            return text_content
                    else:
                        raise ValueError("XPath não fornecido.")
                
                except PlaywrightTimeoutError:
                    attempt += 1
                    # if not self.headless:
                        # print(f"Tentativa {attempt} falhou devido ao timeout. Tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente
                    page.reload(wait_until="domcontentloaded", timeout=60000)

                
                except Exception as e:
                    attempt += 1
                    # if not self.headless:
                        # print(f"Tentativa {attempt} falhou com erro: {e}. Tentando novamente...")
                    time.sleep(2)
                    page.reload(wait_until="domcontentloaded", timeout=60000)

            # Fecha o navegador se não encontrou o elemento após todas as tentativas
            browser.close()
            return None  # Retorna None se todas as tentativas falharem

    def getPage(self):
        with sync_playwright() as p:
            # Inicia o navegador
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            # Garante que a página seja totalmente carregada antes de buscar o conteúdo HTML
            page.goto(self.url, wait_until="load")
            html_content = page.content()
            browser.close()
            return html_content
        
       
    def pesquisarProduto(self, texto):
        max_attempts = 5  # Número máximo de tentativas
        attempt = 0

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            page.goto(self.url, wait_until="load")  # Certifique-se de que `self.url` está definido corretamente

            while attempt < max_attempts:
                try:
                    # Localiza a caixa de texto e insere o texto
                    element = page.locator(f'xpath={self.xpathPesquisa}')
                    
                    element.fill(texto)
                    
                    time.sleep(2)

                    # Se `self.xpathBotaoPesquisa` estiver definido, localiza e clica no botão
                    if self.xpathBotaoPesquisa:
                        botao_element = page.locator(f'xpath={self.xpathBotaoPesquisa}')
                        botao_element.click()

                    # Aguarda a página carregar após o clique
                    page.locator(self.xpathListaPesquisa).wait_for(state="visible", timeout=5000)  # Aguarda elemento aparecer
                    # Captura a URL da página carregada
                    url_atual = page.url

                    # Extrai os conteúdos dos elementos localizados por `self.xpathListaPesquisa`
                    # if self.xpathListaPesquisa:
                    #     conteudos = page.locator(f'xpath={self.xpathListaPesquisa}').all_inner_texts()
                    #     # print(conteudos)
                    # else:
                    #     conteudos = None

                    # Retorna o dicionário com a URL e os conteúdos
                    browser.close()
                    # return {
                    #     "url": url_atual,
                    #     "produtos": conteudos
                    # }
                    
                    return url_atual

                except Exception as e:
                    attempt += 1
                    # print(f"Tentativa {attempt} falhou: {e}. Tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente

            # print("Não foi possível realizar a operação após 5 tentativas.")
            browser.close()
            return None


    def get_link(self, xpath, url):
        with sync_playwright() as p:
            # Inicia o navegador
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            try:
                # Acessa a URL
                page.goto(url, wait_until="load")

                # Localiza os elementos usando o XPath
                elements = page.locator(xpath)

                # Aguarda o elemento aparecer (máximo de 10 segundos)
                elements.wait_for(timeout=10000)

                # Coleta os links encontrados
                links = []
                # if elements.count() > 0:  # Garante que há elementos encontrados
                #     for i in range(elements.count()):
                #         print(i)
                #         html_content = elements.nth(i).inner_html(timeout=5000)
                #         links.extend(self.getHREF(html_content))  # Adiciona links encontrados
                #         print("a\n")
                #         print(links)
                if elements:  # Garante que há elementos encontrados
                    links = self.getHREF(elements.inner_html())
                        
                
                return links if links else None

            except PlaywrightTimeoutError:
                return None
            except Exception as e:
                print(f"Erro inesperado: {e}")
                return None
            finally:
                browser.close()

        
    def getHREF(self, html_content):
        # Padrão para capturar os valores do atributo href com https:// ou /
        pattern = r'href=["\'](https://.*?|/.*?)[\'"]'
        
        # Encontrar todos os links usando a expressão regular
        links = re.findall(pattern, html_content)
        
        # Adicionar self.url aos links relativos
        if self.url is None:
            raise ValueError("self.url não pode ser None")
        links = [self.url + link if link.startswith('/') else link for link in links]
                
        # Aplicar o método maior_prefixo_comum, caso necessário
        links = self.maior_prefixo_comum(links)
        return links


    
    def maior_prefixo_comum(self,lista_strings):
        prefixos = defaultdict(int)  # Dicionário para contar a frequência dos prefixos

        # Para cada string, vamos tentar todos os seus prefixos
        for string in lista_strings:
            for i in range(1, len(string) + 1):
                prefixo = string[:i]
                prefixos[prefixo] += 1

        # Encontrar o prefixo que mais aparece
        if prefixos:
            prefixo_comum = max(prefixos, key=prefixos.get)
        else:
            return None
        # Filtrar as strings que começam com o prefixo mais comum
        resultado = [s for s in lista_strings if s.startswith(prefixo_comum)]

        return resultado
