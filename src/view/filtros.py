import sys
import re
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from controller.loja import LojaController

class Filtros:
    def main():
        
        # # Amazon
        
        # loja = LojaController(r".*R\$", '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]','//*[@id="s-refinements"]/div')

        # categoria1 = loja.getFiltros('https://www.amazon.com.br/s?k=mouse')
        
        # categoria2 = loja.getFiltros('https://www.amazon.com.br/s?k=celular')

        # print(categoria1)
        # print()
        # print(categoria2)
        # print()
        
        # # Mercado livre
        
        # loja = LojaController(r".*R\$",'', '//*[@id="root-app"]/div/div[3]/aside/section[2]')
        
        # categoria1 = loja.getFiltros('https://lista.mercadolivre.com.br/celular#D[A:celular]')
        
        # categoria2 = loja.getFiltros('https://lista.mercadolivre.com.br/nootebook#D[A:nootebook]')

        # print(categoria1)
        # print()
        # print(categoria2)
        # print()
        
        
        # # Pichau
        
        # loja = LojaController(r".*R\$",'', '//*[@id="__next"]/div[1]/main/div[2]/div/div[2]')
        
        # categoria1 = loja.getFiltros('https://www.pichau.com.br/hardware/placa-de-video')
        
        # categoria2 = loja.getFiltros('https://www.pichau.com.br/perifericos/teclado')

        # print(categoria1)
        # print()
        # print(categoria2)
        # print()
        
        
        # ## Farmacias
        
        # loja = LojaController(r".*R\$",'', '//*[@id="__next"]/main/div/div[3]/div/div[1]/div[1]')
        
        # categoria1 = loja.getFiltros('https://www.drogasil.com.br/search?w=hidratante')
        
        # loja = LojaController(r".*R\$",'', '//*[@id="inicio-conteudo"]/div[5]/div/div[2]/aside/div[2]')
        
        # categoria2 = loja.getFiltros('https://www.drogariasaopaulo.com.br/pesquisa?q=hidratante')

        # print(categoria1)
        # print()
        # print(categoria2)
        # print()
        
        entrada = 'CategoriaCelulares e SmartphonesTelefonia FixaTablets, iPads e E-readerÁudioMarcapesquisar por filtroAppleSamsungMotorolaXiaomiOPPOPositivoInfinixLGMultilaser1213C14CA3AlcatelASUSBLUC65C75CATCubotDoogeeE-techGradienteHonorIntelbrasiPhoneitelLenoxxM6MeizuMiyooMotoMultiMulti VitaMutilaserN0TNokiaNotNotePhilcoPoccoPocophonePoçoPσcoR e a l m eRdmRealmeRed MobileRedmSmartSmart IdosoSmartphoneSmartphone 12TCLTecnoUp PlayVitaX i a o m iX6ZTEVer todosPreçoMínimo:R$ 0,00Máximo:R$ 61.369,99Aplicar filtroEntregaMagalu IndicaPromoçõesOfertas do DiaAvaliação54 e acima3 e acima2 e acima1 e acimaVendido porMagaluKaBuM!Loja F7 VariedadesOlist PlusOlist SpBlack WatchZonne StoreOlist StoreLoja King StoreTrocafyLoja Fss VariedadesFranfertec Assistência TécnicaSamsungGbg ImportadosGrupoulalamagazineMagazinemetaImportados Da MiGrupogigacellFonte Das Variedadesgrupo gigaMpeletAllstarFaniquitaAcdigBendezgamesPeletroLmantenas316kmjeletronicosNewdigitalAntoniofortunatodarosaRmazara OnlineNowdigitalRettimportsfelipebentovendaspointeletroLoja iPlacemasterkingeletroCellular StoreecophonenewtelefoniaportalstarFastgoldLojas MastercellstarpointeletroeletronicosesLuivnaManiamixeuromixFaeleletroElittiieletronicosCELLTECHtechonlinedigitalvexmbgamezStarmixinfocelcomerceGaldino Relojoaria E EletrônicosMobcomStoreHtechinfobielzinVer todosTipo de compraCompra nacionalCompra internacionalTipo de produtoCelularCapa para CelularCarregador para Celular e TabletPelícula para CelularKit de Capa e PelículaSmartwatchSuporte para CelularKit de Acessórios para CelularCaboConectorSuporte Automotivo para CelularPulseira para Relógio ou SmartwatchFone de OuvidoControle remotoFonte de AlimentaçãoTripéCapa para SmartwatchMonopodAlmofadaBateria para CelularTapeteIluminador para Fotografia e FilmagemBateria para NotebookLED para TVCapacitorBolsaPelícula para SmartwatchAdaptador EletrônicoTampa TraseiraCaixa de SomMouse padVálvula para LavadoraMicrofonePlaca Eletrônica para Ar CondicionadoKit Reparo para CelularPlaca para TVDobradiçaPocheteProjetorLente de Câmera de CelularSuporte para TabletPé para EletrodomésticosSensor para EletrodomésticosJogo AmericanoCapa para MalaTela Frontal para CelularCabo LightningFlex ConectorLâmpada para EletrodomésticosControle para Celular e TabletAnel para LavadoraLumináriaJogo de Chave de PrecisãoFiltro de Água para RefrigeradorCentral MultimídiaPuxador para EletrodomésticosPeças e Acessórios para EletrodomésticosEstabilizador para CelularBalançaBraçadeira para CelularVer todosArmazenamento InternoAbaixo de 8GB8GB16GB32GB64GB128GB256GB512GB1TBVer todosCorAmareloAura GlowAzulAzul CobaltoBEGEBrancoBronzeChampagneChumboCINZACobreCREMEDouradoLARANJALilásMARROMPRATA PretoPreto e LaranjaPRETO E VERMELHOROSARose GoldROSêRoxoTitânioVerdeVERMELHOÍndigoVer todosMemória RAMAbaixo de 2GB2GB a 3.99GB4GB a 8GBAcima de 8GBTamanho da TelaAbaixo de 5"5" a 5.9"6" a 6.9"7" a 7.9"8" a 8.9"Acima de 10"Ver todosRede Móvel5G4G3G2GCondição UsadoNão aplicável'
        
        def TratamentoFiltros(filtro):
                
                return filtro
            
        
        filtros = TratamentoFiltros(entrada)
        
        for f in filtros:
            print(f)
        
        
        pass
        
    