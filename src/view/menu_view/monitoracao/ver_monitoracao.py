from controller.database import DatabaseController
from src.model.produto import Produto


def ver_monitoracao(ProdutoEntrada):
    database = DatabaseController()
    monitoria = database.sqlRead(f"SELECT * FROM public.monitoria where url = '{ProdutoEntrada[1]}';")
    
    if monitoria != None:
        i = 1
        print()
        for monitor in monitoria:
            print(f"Monitoria {i}")
            print(f"URL: {monitor['url']}")
            print(f"Data: {monitor['date']}")
            print(f"Freqüência(min): {monitor['minuto']}")
            print()
            i+=1
    Produto().gerarGraficoPreco(ProdutoEntrada)

    while True:
        deletar = input("Deseja deletar alguma monitoria(S/N): ").lower()
        if deletar == "s":
            while True:
                deletar = input("Deseja deletar qual item: ")
                if deletar.isdigit() and int(deletar)>=1 and int(deletar)<=i:
                    monitor = monitoria[int(deletar)-1]
                    url = monitor['url']
                    data = monitor['date']
                    minuto = monitor['minuto']
                    database.sqlWrite(f"DELETE FROM public.monitoria WHERE url='{url}' and date = '{data}' and minuto = '{minuto}';")
                    break
                else:
                    print("Entrada inválida")
        elif deletar == "n":  
            break
