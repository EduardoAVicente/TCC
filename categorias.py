from loja import loja
#from compare_lists import compare_lists
from Word2Vec import Word2Vec
from SpaCy import compare_lists
import os

amazon = loja(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]','//*[@id="s-refinements"]/div')

amazon_um = amazon.getFiltros('https://www.amazon.com.br/s?k=mouse')


amazon_dois = amazon.getFiltros('https://www.amazon.com.br/s?k=celular')


os.system('clear')

print(amazon_um)
print()
print(amazon_dois)
print()


# try:
#     result = compare_lists(amazon_um, amazon_dois)

#     # Exibindo resultados
#     for word1, word2, score in result:
#         print(f"{word1} é similar a {word2} com uma pontuação de {score}")
# except ValueError as e:
#     print(e)



# resultados = Word2Vec(amazon_um, amazon_dois)

# # Exibindo os resultados
# for palavra1, palavra2, similaridade in resultados:
#     print(f"'{palavra1}' é similar a '{palavra2}' com uma pontuação de {similaridade}")



resultados = compare_lists(amazon_um, amazon_dois)

# Exibir resultados
for (text1, text2), similarity in resultados.items():
    print(f'Similaridade entre "{text1}" e "{text2}": {similarity:.2f}')