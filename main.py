from loja import loja

amazon = loja('%(.*)', '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]')
# amazon = loja('//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]')
preco = amazon.getPrice('https://www.amazon.com.br/Mouse-Recarregavel-Wireless-Notebook-Desktop/dp/B0C5148YPG/ref=asc_df_B0C5148YPG/?tag=googleshopp00-20&linkCode=df0&hvadid=647471420617&hvpos=&hvnetw=g&hvrand=54754294666624426&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001765&hvtargid=pla-2201447566738&mcid=ee05a775963e30c89f552f6b1d2db180&th=1')

# print(amazon.getPage('https://www.amazon.com.br/Mouse-Recarregavel-Wireless-Notebook-Desktop/dp/B0C5148YPG/ref=asc_df_B0C5148YPG/?tag=googleshopp00-20&linkCode=df0&hvadid=647471420617&hvpos=&hvnetw=g&hvrand=54754294666624426&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001765&hvtargid=pla-2201447566738&mcid=ee05a775963e30c89f552f6b1d2db180&th=1'))

print("Amazon: " + preco)


# mercadolivre = loja([r'R\$\s?(\d+([.,]\d{1,2})?)'], '//*[@id="price"]/div/div[1]/div[1]/span/span')
# preco = mercadolivre.getPrice('https://produto.mercadolivre.com.br/MLB-3795810973-skate-waveboard-2-rodas-87-cm-radical-envio-full-_JM?variation=#reco_item_pos=2&reco_backend=ranker-retrieval-v2p_marketplace&reco_backend_type=low_level&reco_client=vip-v2p&reco_id=86b2dfc9-cd75-43e8-a8af-cfe4b05bed02')

# print("Mercado livre: " + preco)
