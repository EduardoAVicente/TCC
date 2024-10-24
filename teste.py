from loja import loja

import os

mercadolivre = loja(r".*R\$",'', '//*[@id="root-app"]/div/div[3]/aside/section[2]')

mercadolivre_um = mercadolivre.getFiltros('https://lista.mercadolivre.com.br/celular#D[A:celular]')


print(mercadolivre_um)
print()

americanas = loja(r".*R\$",'', '//*[@id="rsyswpsdk"]/div/main/div/div[2]')

americanas_um = americanas.getFiltros('https://www.americanas.com.br/busca/celular')


print(americanas_um)
print()