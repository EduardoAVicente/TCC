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
                
                
    # print(filtros[0])
    # print()
    # print(filtros[1])
    
    # if len(filtros) > 1 and filtros[0] and filtros[1]:
    #     filtragem = smith_waterman(filtros[0],filtros[1])
    
    

    # print(filtragem)
    
    filtro1 = [' economiza freteEm carrinhos de comprasFrete grátisMilhares de produtos do mundo todo na sua casaMarcaSamsung', 'Xiaomi', 'Motorola', 'Apple', 'LG', 'Multilaser', 'Positivo', 'Nokia', 'Realme', 'Mostrar maisModelo13C', 'Poco C65', 'Note 13 Pro 5G', '14c', 'iPhone 11', 'A3', 'P41', 'iPhone 14', 'Mostrar maisMemória internaMenos de 32 GB', '32 a 127 GB', '128 a 255 GB', '256 a 511 GB', '512 GB ou mais', 'CondiçãoNovo', 'Usado', 'Recondicionado', 'Tipo de envio', 'Custo do freteFrete grátis', 'PreçoAté R$ 600', 'R$600 a R$1.000', 'Mais de R$1.000', 'PagamentoParcelamento sem juros', 'DescontosMais de 5% OFF', 'Mais de 10% OFF', 'Mais de 15% OFF', 'Mais de 20% OFF', 'Mais de 25% OFF', 'Mais de 30% OFF', 'Mais de 40% OFF', 'Mais de 50% OFF', 'Lojas oficiaisSomente lojas oficiais', 'Origem do freteLocal', 'Internacional', 'LocalizaçãoSão Paulo', 'Minas Gerais', 'Paraná', 'Rio Grande do Sul', 'Rio de Janeiro', 'Bahia', 'Goiás', 'Santa Catarina', 'Mato Grosso do Sul', 'Mostrar maisMemória RAMMenos de 3 GB', '3 a 5 GB', '6 a 11 GB', '12 GB ou mais', 'Rede móvel2G', '3G', '4G', '5G', '3G, 2G, Wi-fi', '4G/LTE', 'LinhaRedmi', 'Galaxy A', 'Moto G', 'Galaxy S', 'POCO', 'Galaxy J', 'Moto E', 'Galaxy', 'Edge', 'Mostrar maisTamanho da telaMenos de 6,1 "', '6,1 a 6,4 "', '6,5 a 6,57 "', '6,67 a 6,74 "', '6,74 " ou mais', 'Resolução da câmera traseira principal13 Mpx ou menos', '13 a 49 Mpx', '50 a 63 Mpx', '64 Mpx ou mais', 'Resolução da câmera frontal principal8 Mpx ou menos', '8 a 9 Mpx', '10 a 31 Mpx', '32 Mpx ou mais', 'OperadoraDesbloqueado', 'Vivo', 'Claro', 'TIM', 'Nextel', 'Oi', 'Nome do sistema operacionalAndroid', 'iOS', 'KaiOS', 'Symbian', 'S30+', 'Nokia', 'Windows Phone', 'BlackBerry OS', 'Andriod/Redmagic', 'Detalhes do anúncioMelhores vendedores', 'Outras pessoas pesquisaramcelular ate 500 00celular ephonecelular xiani notecekucelular 📲']
    filtro2 = ['Ofertas e Descontos', 'Ofertas Black Friday', 'Elegível a Frete Grátis', 'Frete Grátis em envios pela Amazon', 'Todos os clientes têm frete GRÁTIS em pedidos a partir de R$ 129 em produtos enviados pela Amazon.', 'Departamento', 'Celulares e Comunicação', 'Celulares e Smartphones', 'Celulares básicos', 'Avaliação do Cliente', 'Quatro estrelas e acima', 'e acima', 'Marcas', 'Motorola', 'SAMSUNG', 'Xiaomi', 'Apple', 'Multilaser', 'realme', 'Positivo', 'Infinix', 'Nokia', 'Redmi', 'Geonav', 'Gshield', 'I2GO', 'Coibeu', 'Danet', 'Basike', 'NO2PROBLEMS', 'intelbras', 'CASETiFY', 'ONYK', 'JBL', 'GameSir', 'Baseus', 'ULANZI', 'Hmaston', 'GTI Expressa', 'Ipega', 'NANU SHOP', 'Gorila Shield', 'Vinwer', 'Zhiyun', 'Utilibrox', 'Dpofirs', 'Logitech', 'hohem', 'ENCASED', 'Legado Engenharia', 'Lenoxx', 'Carphone Warehouse', 'ELG', 'Ver mais', 'Flash da câmera', 'Flash da câmara frontal', 'LED', 'LED duplo', 'Preços', 'R$1', 'R$26.600 e mais', 'Ir', 'Condição', 'Novo', 'Usado', 'Sistema operacional', 'Android 10.0', 'Android 11.0', 'Android 12.0', 'Android 13.0', 'Android 9.0', 'iOS 14', 'iOS 16', 'Android 4.0', 'Android 5.0', 'Android 6.0', 'iOS 15', 'MIUI 11', 'MIUI 12', 'MIUI 12.5', 'Ver mais', 'Capacidade de Armazenamento de Memória do Telefone Celular', 'Até 3,9 GB', '4 GB', '8 GB', '16 GB', '32 GB', '64 GB', '128 GB', '256 GB', '512 GB ou mais', 'Resolução da Câmera de Telefone Celular', '5 - 7,9 MP', '8 - 12,9 MP', '13 - 19,9 MP', '20 MP ou Mais', 'Peso do produto', 'Até 141,9 g', '142 a 197,9 g', '198 a 254,9 g', '255 g ou mais', 'Tamanho da tela', 'Menos de 3,9 Polegadas', '4,5 a 4,9 Polegadas', '5,5 Polegadas ou Mais', 'Fator forma', 'Ardósia', 'Barra', 'Capa dobrável', 'Deslizante', 'Tela dobrável', 'Capacidade da bateria', 'Até 2.999 mAh', '3.000 a 3.999 mAh', '4.000 a 4.999 mAh', '5.000 a 5.999 mAh', '6.000 mAh e mais', 'Tamanho do cartão SIM', 'Nano', 'Tecnologia de Conectividade de Telefone Celular', 'Bluetooth', 'Infravermelho', 'NFC', 'USB', 'Wi-Fi', 'Tipo de tela', 'AMOLED', 'LCD', 'OLED', 'Componentes incluídos', 'Capa de celular', 'Adaptador de alimentação', 'Ejetor da bandeja SIM', 'Caneta stylus', 'Cabo USB', 'Adaptador de áudio', 'Auscultadores', 'Protetor de tela', 'Ver mais', 'Modos de Filmagem do Telefone Celular', 'Automático', 'Cena', 'Esportes', 'Grande alcance dinâmico', 'Macro', 'Manual', 'Modo noturno', 'Panorama', 'Prioridade de abertura', 'Retrato', 'Ver mais', 'Entrada de fone de ouvido', '3.5 mm', 'Resolução do sensor fotográfico frontal', 'Até 6,9 MP', '7,0 a 9,9 MP', '10,0 a 12,9 MP', '13,0 MP ou mais', 'GPS', 'Falso', 'Verdadeiro', 'Recurso de segurança biométrica do celular', 'Reconhecimento da íris', 'Reconhecimento de impressões digitais', 'Reconhecimento facial', 'Taxa de atualização da tela', 'Até 88 Hz', '89 a 104 Hz', '105 a 120 Hz', '121 Hz ou mais', 'Entrada de Interface Humana do Telefone Celular', 'Botões', 'OCR', 'Teclado', 'Teclado numérico', 'Microfone', 'Teclado Numérico', 'Touch Pad', 'Tela Sensível ao Toque', 'Tela sensível ao toque com suporte para caneta Stylus', 'Ver mais', 'Contagem de slots do cartão SIM', 'SIM único', 'Dual SIM', 'Tipo de Conector de Telefone Celular', 'Entrada de 3,5 mm', 'Lightning', 'Micro USB', 'Mini USB', 'USB tipo C', 'Resolução do Telefone Celular', '1080 x 2160', '1080 x 2340', '1080 x 2400', '1280 x 720', '1600 x 720', '1920 x 1080', '2340 x 1080', '240 x 320', '2400 x 1080', '2532 x 1170', '2640x1080', '320 x 240', '720 x 1520', '720 x 1600', 'Ver mais', 'Características do material', 'Reciclável', 'Resistente à temperatura', 'Descrição da bateria', 'Íon de lítio', 'Polímero de lítio', 'Tecnologia de rede sem fios', 'CDMA', 'GSM', 'LTE', 'UMTS', 'Wi-Fi', 'Resolução de captura de vídeo', '1080p', '2k', '4k', '720p', '8k', 'Sistema de navegação por satélite suportado', 'GLONASS', 'GPS', 'Celular Foto sensor resolução', 'Até 9.9 MP', '10 a 12,9 MP', '13 a 15,9 MP', '16 MP ou Mais', 'Duração média da bateria do telefone celular', 'Até 6,9 h', '7 a 12,9 h', '13 a 18,9 h', '19 h ou Mais', 'Tecnologias de rede móvel', '2G', '3G', '4G', '5G', 'Tamanho da Memória RAM Instalada do Telefone Celular', 'Até 1,9 GB', '2 a 3,9 GB', '4 a 5,9 GB', '6 a 7,9 GB', '8 a 9,9 GB', '10 GB ou Mais', 'Programe e Poupe', 'Compras recorrentes com desconto', 'Novidades', 'Últimos 30 dias', 'Últimos 90 dias', 'Disponibilidade', 'Exibir Itens sem Estoque']
    
    filtragem = smith_waterman(filtro1,filtro2)
    
    i = 1
    if filtragem:
        if len(filtragem) > 0:
            print("Filtros encontrados:")
            for f in filtragem:
                print(f"{i}. {f}")
                i+=1
    
   
    # Busca o produto
    
    for i in range(len(lojas)):
        scrapper = ScrapperController(url=lojas[i]['url'])
        
        links = scrapper.get_link(lojas[i]['xpathlistapesquisa'],urls[i])
        if links:
            for link in links:
                produto = ProdutoController(lojas[i]['regexproduto'],lojas[i]['xpathproduto'],link)
                if produto.getPrice() != None:
                    break
    
        
