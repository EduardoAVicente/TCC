import re
import sys
sys.path.append(".")
from src.view.menu_view.produto.adicionar_produto import gerarNomeSite

def test_gerarNomeSite():
    result = gerarNomeSite('https://www.amazon.com.br/Mouse-Recarregavel-Wireless-Notebook-Desktop/dp/B0C5148YPG/ref=asc_df_B0C5148YPG/?tag=googleshopp00-20&linkCode=df0&hvadid=647471420617&hvpos=&hvnetw=g&hvrand=54754294666624426&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1001765&hvtargid=pla-2201447566738&mcid=ee05a775963e30c89f552f6b1d2db180&th=1')
    assert result == 'amazon'
    
    result = gerarNomeSite('https://produto.mercadolivre.com.br/MLB-4808560368-mouse-gamer-dpi-3600-transparente-led-6-botoes-tiger-chroma-_JM#polycard_client=recommendations_pdp-pads-up&reco_backend=recos-merge-experimental-pdp-up-c_marketplace&reco_client=pdp-pads-up&reco_item_pos=1&reco_backend_type=low_level&reco_id=3fab6d28-d129-4140-8afb-1bbf753b6cf0&is_advertising=true&ad_domain=PDPDESKTOP_UP&ad_position=2&ad_click_id=M2NmM2VjNmUtNTEyZC00MTcyLTg4OGUtODdjNWRkN2UzZDU2')
    assert result == 'mercadolivre'
    
    result = gerarNomeSite('https://pt.aliexpress.com/item/1005007185469339.html?src=google&src=google&albch=shopping&acnt=768-202-3196&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005007185469339&ds_e_product_merchant_id=5386383474&ds_e_product_country=BR&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=21451868324&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=CjwKCAjwl6-3BhBWEiwApN6_kjb6NgRqvEIz9UHm-gXPmxuG_gp0XfMIEbrcF56WSwodI5ygOyKWSxoCncMQAvD_BwE')
    assert result == 'aliexpress'
    