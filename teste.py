from loja import loja
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

amazon = loja(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]','//*[@id="s-refinements"]/div')

amazon_um = amazon.getFiltros('https://www.amazon.com.br/s?k=mouse')


print('Amazon: ' , end="")
print(amazon_um)
print('\n')



mercadolivre = loja(r".*R\$",'', '//*[@id="root-app"]/div/div[3]/aside/section[2]')

mercadolivre_um = mercadolivre.getFiltros('https://lista.mercadolivre.com.br/celular#D[A:celular]')

print('Mercado Livre: ' , end="")
print(mercadolivre_um)
print()



# americanas = loja(r".*R\$",'', '//*[@id="rsyswpsdk"]/div/main/div/div[2]')

# americanas_um = americanas.getFiltros('https://www.americanas.com.br/busca/celular')

# print('Americanas: ', end="")
# print(americanas_um)
# print()
