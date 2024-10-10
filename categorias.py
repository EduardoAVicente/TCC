from loja import loja

amazon = loja(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]','//*[@id="s-refinements"]/div')

amazon.getFiltros('https://www.amazon.com.br/s?k=mouse')


amazon.getFiltros('https://www.amazon.com.br/s?k=celular')