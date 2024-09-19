from playwright.sync_api import sync_playwright
import time

class Scrapper:
    def __init__(self, url, xpath):
        self.url = url
        self.xpath = xpath

    def get_element_value(self):
        max_attempts = 5  # Número máximo de tentativas
        attempt = 0

        with sync_playwright() as p:
            # Inicie o navegador
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)
            
            if self.xpath:
                while attempt < max_attempts:
                    try:
                        # Tenta localizar o elemento
                        element = page.locator(f'xpath={self.xpath}').first
                        # Verifica se o conteúdo do texto foi encontrado
                        text_content = element.text_content(timeout=5000)
                        if text_content:
                            return text_content
                    except Exception as e:
                        # Caso a tentativa falhe, incrementa o contador e espera 2 segundos
                        attempt += 1
                        print(f"Tentativa {attempt} falhou. Dando refresh e tentando novamente...")
                        time.sleep(2)
                        page.reload()  # Atualiza a página antes de tentar novamente
                
                return f"Elemento não encontrado após {max_attempts} tentativas."
            else:
                return "XPath não fornecido."
            
            browser.close()

    def getPage(self):
        with sync_playwright() as p:
            # Inicie o navegador
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            html_content = page.content()
            browser.close()
            return html_content
