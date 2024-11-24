from controller.loja import LojaController
from controller.nlp_tools.smith_waterman import smith_waterman
from controller.scrapper import ScrapperController
from controller.produto import ProdutoController


def resultado_pesquisa(lojas, pesquisa):
    urls = []
    filtros = []
    for l in lojas:
        loja = LojaController(regexProduto=l['regexproduto'],xpathProduto=l['xpathproduto'],xpathFiltro=l['xpathfiltro'],xpathPesquisa=l['xpathpesquisa'], xpathBotaoPesquisa=l['xpathbotaopesquisa'],xpathListaPesquisa=l['xpathlistapesquisa'])
        url = loja.pesquisarProduto(l['url'],pesquisa)
        urls.append(url)
    # if len(urls) > 0:
    #     for u in urls:
    #         if u:
    #             filtros.append(loja.getFiltros(u))
    
    # if len(filtros) > 1 and filtros[0] and filtros[1]:
    #     filtros = smith_waterman(filtros[0],filtros[1])
    # else:
    #     filtros = urls[0]
    
    # print(filtros)
    
    # i = 1
    # if filtros:
    #     if len(filtros) > 0:
    #         for f in filtros:
    #             print(f"{i}. {f}")
    #             i+=1
    
   
    
    for i in range(len(lojas)):
        scrapper = ScrapperController(url=lojas[i]['url'])
        
        links = scrapper.get_link(lojas[i]['xpathlistapesquisa'],urls[i])
        if links:
            for link in links:
                produto = ProdutoController(lojas[i]['regexproduto'],lojas[i]['xpathproduto'],link)
                if produto.getPrice() != None:
                    break
    
        
