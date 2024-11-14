from controller.database import DatabaseController
from controller.produto import ProdutoController
from model.produto import Produto
from model.loja import Loja
import schedule
import threading
from datetime import datetime, timedelta
import time


class MonitoracaoController:
    def __init__(self):
        self.database = DatabaseController()
        
    def main(self):
        print("Carregando monitorias...")
        monitoria = self.database.getData("MONITORIA")
        
        print("Agendando monitorias...")
        if monitoria:
            for monitor in monitoria:
                carregarMonitor(monitor)
                
        print("Monitorias agendadas em 2° plano")
        
        # Cria uma nova thread para o loop de agendamento
        agendamento_thread = threading.Thread(target=self.loop_agendamento)
        agendamento_thread.start()
        
    def loop_agendamento(self):
        while True:
            # Executa as tarefas agendadas
            schedule.run_pending()
            
            # Imprime as tarefas agendadas
            jobs = schedule.get_jobs()
            if jobs:
                print("Atividades em espera:")
                for job in jobs:
                    print(f"Próximo agendamento: {job.next_run}")
            else:
                print("Nenhuma atividade em espera.")
            
            time.sleep(1)  # Pausa por um segundo antes de verificar novamente


def carregarMonitor(monitor):
    url = monitor[0]
    data = monitor[1]
    minuto = monitor[2]
    
    # Calcula a nova data e hora com base no intervalo em minutos
    nova_data = data + timedelta(minutes=minuto)
    agora = datetime.now()
    
    if nova_data <= agora:
        # Calcula a diferença para o próximo agendamento em minutos
        diferenca_em_minutos = 0  # Defina um valor de tempo válido para o agendamento
        print(f"Agendando tarefa para {diferenca_em_minutos} minutos após a execução.")
        schedule.every(diferenca_em_minutos).minutes.do(rodar_task_em_thread, url, diferenca_em_minutos)
    else:
        print("A tarefa não está agendada para o horário atual ou futuro próximo.")



def rodar_task_em_thread(url, diferenca_em_minutos):
    # Cria uma nova thread para executar a tarefa em segundo plano
    task_thread = threading.Thread(target=task, args=(url, diferenca_em_minutos))
    task_thread.start()


def task(url, diferenca_em_minutos):
    print("Inico task")
    # produto = ProdutoController(Loja().getRegex(url), Loja.getXpathProduto(url), url)
    # produto.getPrice()
    print(f"Monitoração de {url} concluída com sucesso!")
    
    # Reagendar a tarefa
    
    schedule.every(diferenca_em_minutos).minutes.do(rodar_task_em_thread, url, diferenca_em_minutos)
