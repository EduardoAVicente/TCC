import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from model.database import Database

class Auxiliar:
    def main():
        database = Database()
        print(database.getProducts())