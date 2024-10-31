from playwright.sync_api import sync_playwright
import time

class ScrapperController:
    def __init__(self, url, xpath):
        self.url = url
        self.xpath = xpath
        self.headless = False

    def get_element_value(self):
        max_attempts = 5  # Número máximo de tentativas
        attempt = 0

        with sync_playwright() as p:
            # Inicia o navegador
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            # Garante que a página seja totalmente carregada antes de buscar o elemento
            page.goto(self.url, wait_until="load")
            
            if self.xpath:
                while attempt < max_attempts:
                    try:
                        # Tenta localizar o elemento
                        element = page.locator(f'xpath={self.xpath}').first
                        # Aguarda até que o conteúdo do texto seja acessível
                        text_content = element.text_content(timeout=5000)
                        if text_content:
                            return text_content
                    except Exception as e:
                        # Caso a tentativa falhe, incrementa o contador e espera 2 segundos
                        attempt += 1
                        if not self.headless:
                            print(f"Tentativa {attempt} falhou. Dando refresh e tentando novamente...")
                        time.sleep(2)
                        # Recarrega a página e espera que seja totalmente carregada novamente
                        page.reload(wait_until="load")
                
                return None
            else:
                raise ValueError("XPath não fornecido.")
            
            browser.close()

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