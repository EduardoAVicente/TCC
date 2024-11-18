import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.loja import LojaController

class Filtros:
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
        
        
        # Pichau
        
        loja = LojaController(r".*R\$",'', '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]')
        
        categoria1 = loja.getFiltros('https://www.pichau.com.br/hardware/placa-de-video')
        
        categoria2 = loja.getFiltros('https://www.pichau.com.br/perifericos/teclado')

        print(categoria1)
        print()
        print(categoria2)
        print()
        
        
        ## Farmacias
        
        loja = LojaController(r".*R\$",'', '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]')
        
        categoria1 = loja.getFiltros('https://www.drogasil.com.br/search?w=hidratante')
        
        loja = LojaController(r".*R\$",'', '//*[@id="inicio-conteudo"]/div[5]/div/div[2]/aside/div[2]')
        
        categoria2 = loja.getFiltros('https://www.drogariasaopaulo.com.br/pesquisa?q=hidratante')

        print(categoria1)
        print()
        print(categoria2)
        print()
        pass
        
        