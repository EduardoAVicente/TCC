from playwright.sync_api import sync_playwright

class Scrapper:
    def __init__(self, url, xpath=None):
        self.url = url
        self.xpath = xpath

    def get_element_value(self):
        with sync_playwright() as p:
            # Inicie o navegador
            browser = p.chromium.launch(headless=True)  # O parâmetro headless é equivalente ao --headless no Selenium
            page = browser.new_page()
            page.goto(self.url)
            
            if self.xpath:
                # Use o XPath para encontrar o elemento e obter seu valor
                try:
                    element = page.locator(f'xpath={self.xpath}')
                    return element.text_content()
                except Exception as e:
                    return str(e)
            else:
                return "XPath não fornecido."
            
            browser.close()

    def get_page(self):
        with sync_playwright() as p:
            # Inicie o navegador
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(self.url)
            html_content = page.content()
            browser.close()
            return html_content
