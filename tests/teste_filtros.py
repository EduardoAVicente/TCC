import sys
sys.path.append(".")
from src.controller.loja import LojaController

loja = LojaController()

def test_TratamentoFiltros():
    loja.TratamentoFiltros()