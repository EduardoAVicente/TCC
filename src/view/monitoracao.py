import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.database import DatabaseController
from model.produto import Produto
from model.loja import Loja
from controller.loja import LojaController

class Monitoracao:
    def main():
        # amazon = LojaController(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]')


        # amazon.addProduto('https://www.amazon.com.br/Mouse-Recarregavel-Wireless-Notebook-Desktop/dp/B0C5148YPG/ref=asc_df_B0C5148YPG/?tag=googleshopp00-20&linkCode=df0&hvadid=647471420617&hvpos=&hvnetw=g&hvrand=54754294666624426&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001765&hvtargid=pla-2201447566738&mcid=ee05a775963e30c89f552f6b1d2db180&th=1')

        # amazon.addProduto("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1")

        # amazon.atualizaProdutos()



        mercadolivre = LojaController(r"R\$", '//*[@id="price"]/div/div[1]/div[1]/span/span')

        mercadolivre.addProduto('https://produto.mercadolivre.com.br/MLB-4808560368-mouse-gamer-dpi-3600-transparente-led-6-botoes-tiger-chroma-_JM#polycard_client=recommendations_pdp-pads-up&reco_backend=recos-merge-experimental-pdp-up-c_marketplace&reco_client=pdp-pads-up&reco_item_pos=1&reco_backend_type=low_level&reco_id=3fab6d28-d129-4140-8afb-1bbf753b6cf0&is_advertising=true&ad_domain=PDPDESKTOP_UP&ad_position=2&ad_click_id=M2NmM2VjNmUtNTEyZC00MTcyLTg4OGUtODdjNWRkN2UzZDU2')

        mercadolivre.addProduto("https://produto.mercadolivre.com.br/MLB-3732772695-mouse-gamer-optico-rgb-magegee-6-nivel-dpi-7-botoes-g10-_JM#polycard_client=recommendations_vip-pads-up&reco_backend=vip_pads_up_ranker_retrieval_system_ctr_odin_marketplace&reco_client=vip-pads-up&reco_item_pos=2&reco_backend_type=low_level&reco_id=b310e075-efc7-46be-b9d6-0b68b9281f04&is_advertising=true&ad_domain=VIPDESKTOP_UP&ad_position=3&ad_click_id=YWI3N2JmOTAtZDc4OS00M2Y2LWEzNTMtZGU4MTdmODYwNTgz")

        mercadolivre.atualizaProdutos()



        # aliexpress = LojaController(r"R\$", '//*[@id="root"]/div/div[1]/div/div[1]/div[1]/div[2]/div[2]/div[1]/span')

        # aliexpress.addProduto('https://pt.aliexpress.com/item/1005007185469339.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005007185469339&ds_e_product_merchant_id=5386383474&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21451868324&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwl6-3BhBWEiwApN6_kjb6NgRqvEIz9UHm-gXPmxuG_gp0XfMIEbrcF56WSwodI5ygOyKWSxoCncMQAvD_BwE')

        # aliexpress.addProduto('https://pt.aliexpress.com/item/1005007067626299.html?src=google&src=google&albch=shopping&acnt=548-301-0399&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005007067626299&ds_e_product_merchant_id=5373267315&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20672963503&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwl6-3BhBWEiwApN6_kgTlYzK26oqF_it7Yeb6AR2uGDuIiAaSgkrHgtIE8wo9tTCpqBHnZRoCGY4QAvD_BwE')

        # aliexpress.atualizaProdutos()

        # kabum = LojaController(r'R\$ ', '//*[@id="blocoValores"]/div[3]/div[1]/div/h4')

        # kabum.addProduto('https://www.kabum.com.br/produto/520369/processador-amd-ryzen-7-5700x3d-3-6-ghz-4-1ghz-max-turbo-cache-4mb-8-nucleos-16-threads-am4-100-100001503wof')

        # kabum.atualizaProdutos()  
        
        # produto = Produto()
        
        # print(produto.getName("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1"))
        # print(produto.getSite('https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1'))
        
        # loja = Loja()
        
        # print(loja.getXpathProduto("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1"))
        # print(loja.getXpathFiltro("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1"))
        # print(loja.getXpathPesquisa("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1"))
        # print(loja.getXpathBotaoPesquisa("https://www.amazon.com.br/Teclado-Nanoreceptor-Inclusas-Logitech-Teclados/dp/B07643MPGS/ref=pd_bxgy_d_sccl_1/141-0794179-5287360?pd_rd_w=Wcuuq&content-id=amzn1.sym.24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_p=24c12540-16c9-4f25-a9fc-1d03ac7f6922&pf_rd_r=RD1E7VEWPTWV261W520Z&pd_rd_wg=1wayP&pd_rd_r=ff1c10ea-955c-4fb7-a107-0683e53e74d2&pd_rd_i=B07643MPGS&psc=1"))
        pass
    
        db_controller = DatabaseController()  # Crie a instância
        data = db_controller.sqlRead(f"select regexproduto, xpathproduto, url from product p join loja l on l.site = p.site where regexproduto is not null and xpathproduto is not null;")

        for d in data:
            loja = LojaController(d['regexproduto'], d['xpathproduto'])
            loja.addProduto(d['url'])
            loja.atualizaProdutos()