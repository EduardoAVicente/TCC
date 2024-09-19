from loja import loja


# amazon = loja(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]')

amazon = loja("", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]')

amazon.addProduto('https://www.amazon.com.br/Mouse-Recarregavel-Wireless-Notebook-Desktop/dp/B0C5148YPG/ref=asc_df_B0C5148YPG/?tag=googleshopp00-20&linkCode=df0&hvadid=647471420617&hvpos=&hvnetw=g&hvrand=54754294666624426&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001765&hvtargid=pla-2201447566738&mcid=ee05a775963e30c89f552f6b1d2db180&th=1')

amazon.addProduto("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1")

amazon.atualizaProdutos()


# mercadolivre = loja([r'R\$\s?(\d+([.,]\d{1,2})?)'], '//*[@id="price"]/div/div[1]/div[1]/span/span')

# mercadolivre = loja("", '//*[@id=":R56ick4um:"]/li[2]/div/div[2]/div/div/div/div[1]/span')

# mercadolivre.addProduto('https://www.mercadolivre.com.br/mouse-gamer-logitech-g203-lightsync-rgb-ate-8000-dpi-branco/p/MLB16211423#wid%3DMLB1813858187%26sid%3Dsearch%26searchVariation%3DMLB16211423%26position%3D2%26search_layout%3Dgrid%26type%3Dproduct%26tracking_id%3Dd13e34f9-3cff-4e05-8c1e-dde931ec68f5')

# mercadolivre.atualizaProdutos()
