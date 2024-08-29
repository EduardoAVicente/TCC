from playwright.sync_api import sync_playwright

class Scrapper:
    def __init__(self, url, xpath=None):
        self.url = url
        self.xpath = xpath

    def get_element_value(self):
        with sync_playwright() as p:
            # Inicie o navegador
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(self.url)
            
            if self.xpath:
                try:
                    # Aumentar o tempo de espera para o localizador
                    element = page.locator(f'xpath={self.xpath}').first
                    return element.text_content()
                except Exception as e:
                    return str(e)
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
