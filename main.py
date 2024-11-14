
import sys
from src.view.monitoracao import Monitoracao
from src.view.avaliacaoNLP import AvaliacaoNLP
from src.view.filtros import Filtros
from src.view.menu import Menu
from src.controller.monitoracao import MonitoracaoController
import time




# MonitoracaoController().main()
# time.sleep(5)

if __name__ == "__main__":
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
            case _:
                print("Função invalida")
    elif len(sys.argv) == 1:
        Menu.main()
    else:
        print("Função invalida")
