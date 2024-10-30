import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.loja import LojaController

class Auxiliar:
    def main():
        
        # Amazon
        
        loja = LojaController(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]','//*[@id="s-refinements"]/div')

        categoria1 = loja.getFiltros('https://www.amazon.com.br/s?k=mouse')
        
        categoria2 = loja.getFiltros('https://www.amazon.com.br/s?k=celular')

        print(categoria1)
        print()
        print(categoria2)
        print()
        
        # Mercado livre
        
        loja = LojaController(r".*R\$",'', '//*[@id="root-app"]/div/div[3]/aside/section[2]')
        
        categoria1 = loja.getFiltros('https://lista.mercadolivre.com.br/celular#D[A:celular]')
        
        categoria2 = loja.getFiltros('https://lista.mercadolivre.com.br/nootebook#D[A:nootebook]')

        print(categoria1)
        print()
        print(categoria2)
        print()