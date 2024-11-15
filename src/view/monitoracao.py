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

        db_controller = DatabaseController()  # Crie a instância
        data = db_controller.sqlRead(f"select regexproduto, xpathproduto, url from product p join loja l on l.site = p.site where regexproduto is not null and xpathproduto is not null;")

        for d in data:
            loja = LojaController(d['regexproduto'], d['xpathproduto'])
            loja.addProduto(d['url'])
            loja.atualizaProdutos()