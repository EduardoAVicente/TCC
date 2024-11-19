from controller.loja import LojaController

def resultado_pesquisa(lojas, pesquisa):
    # for l in lojas:
    #     print(l)
    
        # if url['url']:
            #     filtro = loja.getFiltros(url['url'])
            #     print(filtro)
        
        
        loja = LojaController(xpathFiltro=l['xpathfiltro'],xpathPesquisa=l['xpathpesquisa'], xpathBotaoPesquisa=l['xpathbotaopesquisa'],xpathListaPesquisa=l['xpathlistapesquisa'])
        busca = loja.pesquisarProduto('https://www.mercadolivre.com.br/',pesquisa)
        
        print(busca['produtos'])
        
        
 
        
