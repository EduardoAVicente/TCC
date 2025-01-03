import sys
import time
import threading
from src.view.monitoracao import Monitoracao
from src.view.avaliacaoNLP import AvaliacaoNLP
from src.view.filtros import Filtros
from src.view.menu import Menu
from src.controller.monitoracao import MonitoracaoController
from src.controller.scrapper import ScrapperController
from src.view.simulacaoSmithWaterman import simulacaoSmithWaterman
# from src.view.grafico import gerarGrafico


# def executar_monitoracao():
#     MonitoracaoController().main()

# if __name__ == "__main__":
#     # Cria uma thread para executar MonitoracaoController().main() em segundo plano
#     thread_monitoracao = threading.Thread(target=executar_monitoracao)
#     thread_monitoracao.start()

#     # Pausa por 5 segundos para garantir que a thread de monitoramento esteja rodando
#     time.sleep(5)

if len(sys.argv) > 1:
    palavra = sys.argv[1].lower()
    match palavra:
        case "monitoracao":
            Monitoracao.main()
        case "nlp":
            avaliacao = AvaliacaoNLP()
            avaliacao.main()
        case "auxiliar":
            Filtros.main()
        case "xpath":
            if(len(sys.argv) == 4):
                print(ScrapperController(sys.argv[2]).getXpath(sys.argv[3]))
        # case "grafico":
        #     gerarGrafico()
        case "smithwaterman":
            simulacaoSmithWaterman()
        case _:
            print("Função invalida")
elif len(sys.argv) == 1:
    Menu.main()
else:
    print("Função invalida")
