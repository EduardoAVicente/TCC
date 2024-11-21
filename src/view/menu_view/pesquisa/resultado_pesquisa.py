from controller.loja import LojaController

def resultado_pesquisa(lojas, pesquisa):
    for l in lojas:
        # print(l)
        loja = LojaController(regexProduto=l['regexproduto'],xpathProduto=l['xpathproduto'],xpathFiltro=l['xpathfiltro'],xpathPesquisa=l['xpathpesquisa'], xpathBotaoPesquisa=l['xpathbotaopesquisa'],xpathListaPesquisa=l['xpathlistapesquisa'])
        busca = loja.pesquisarProduto(l['url'],pesquisa)
        
        # print(busca['url'])
        
        # print()
        
        # if busca['url']:
        #     filtro = loja.getFiltros(busca['url'])
        #     print(filtro)
        
        
 
        
