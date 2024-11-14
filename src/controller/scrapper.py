from playwright.sync_api import sync_playwright
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

class ScrapperController:
    def __init__(self, url, xpath):
        self.url = url
        self.xpath = xpath
        self.headless = True

    def get_element_value(self):
        max_attempts = 5  # Número máximo de tentativas
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
                    if not self.headless:
                        print(f"Tentativa {attempt} falhou devido ao timeout. Tentando novamente...")
                    time.sleep(2)  # Espera 2 segundos antes de tentar novamente
                    page.reload(wait_until="load")
                
                except Exception as e:
                    attempt += 1
                    if not self.headless:
                        print(f"Tentativa {attempt} falhou com erro: {e}. Tentando novamente...")
                    time.sleep(2)
                    page.reload(wait_until="load")

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