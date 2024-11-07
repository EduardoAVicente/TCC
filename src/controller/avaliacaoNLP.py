import concurrent.futures
import time
from tabulate import tabulate
from model.avaliacaoNLP import testes

class avaliacaoNLPController:
    def __init__(self, algoritmos):
        self.algoritmos = algoritmos
        self.max_processes = 20  # Define o número máximo de threads simultâneas
        self.resultados_avaliacao = {
            "FP": {alg[0]: 0 for alg in algoritmos},
            "FN": {alg[0]: 0 for alg in algoritmos},
            "VP": {alg[0]: 0 for alg in algoritmos},
            "VN": {alg[0]: 0 for alg in algoritmos}
        }

    def main(self):
        num_testes = len(testes)
        
        # Estruturas para armazenar resultados
        resultados = {alg[0]: ["semelhanca"] + [0] * num_testes for alg in self.algoritmos}
        tempos = {alg[0]: ["tempo"] + [0] * num_testes for alg in self.algoritmos}

        # Executar cada teste em paralelo com limite de threads
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_processes) as executor:
            for i in range(num_testes):
                futures = []
                for algoritmo_nome, algoritmo_func in self.algoritmos:
                    # Submeter a execução de algoritmo_func em paralelo
                    future = executor.submit(self.__executar_algoritmo, algoritmo_nome, algoritmo_func, testes[i], i, resultados, tempos)
                    futures.append(future)
                
                # Aguardar o término de todos os algoritmos para o teste atual
                concurrent.futures.wait(futures)

        # Calcular as médias
        medias_sim = {alg[0]: round(sum(resultados[alg[0]][1:]) / num_testes, 2) for alg in self.algoritmos}
        medias_tempo = {alg[0]: round(sum(tempos[alg[0]][1:]) / num_testes, 2) for alg in self.algoritmos}

        # Imprimir a tabela no formato desejado
        return self.__tabela(resultados, tempos, medias_sim, medias_tempo, num_testes)

    def __executar_algoritmo(self, algoritmo_nome, algoritmo_func, teste, teste_index, resultados, tempos):
        start_time = time.time()
        resultado = algoritmo_func(teste[0], teste[1])
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 4) * 1000
        
        similaridade = 0
        if resultado:
            similaridade = self.__calcular_semelhanca(resultado, teste[2])

        # Armazena os resultados e tempo
        resultados[algoritmo_nome][teste_index + 1] = similaridade
        tempos[algoritmo_nome][teste_index + 1] = elapsed_time

        # Atualizar FP, FN, VP, VN
        self.__atualizar_métricas_avaliacao(algoritmo_nome, resultado, teste[2])

    def __atualizar_métricas_avaliacao(self, algoritmo_nome, resultado, esperado):
        # Normalizar as listas
        resultado_normalizado = {item.strip().lower() for item in resultado} if resultado else set()
        esperado_normalizado = {item.strip().lower() for item in esperado}
        
        # Cálculo de FP, FN, VP, VN
        self.VP = len(resultado_normalizado.intersection(esperado_normalizado))
        self.FP = len(resultado_normalizado - esperado_normalizado)
        self.FN = len(esperado_normalizado - resultado_normalizado)
        self.VN = 0  # Para NLP, o VN pode ser complexa; depende do contexto dos dados

        self.resultados_avaliacao["VP"][algoritmo_nome] += VP
        self.resultados_avaliacao["FP"][algoritmo_nome] += FP
        self.resultados_avaliacao["FN"][algoritmo_nome] += FN
        self.resultados_avaliacao["VN"][algoritmo_nome] += VN

    def __tabela(self, resultados, tempos, medias_sim, medias_tempo, quant_testes):
        headers = ["Algoritmo", "Metricas"] + [f"Teste {i+1}" for i in range(quant_testes)] + ["Média"]
        dados = []
        
        for algoritmo_nome in resultados.keys():
            dados.append([algoritmo_nome, "semelhanca"] + resultados[algoritmo_nome][1:] + [medias_sim[algoritmo_nome]])
            dados.append(["", "tempo"] + [f"{tempo:.2f}ms" for tempo in tempos[algoritmo_nome][1:]] + [f"{medias_tempo[algoritmo_nome]:.2f}ms"])
        
        return tabulate(dados, headers=headers, tablefmt='grid')
    
    def __calcular_semelhanca(self, lista1, lista2):
        lista1_normalizada = {item.strip().lower() for item in lista1}
        lista2_normalizada = {item.strip().lower() for item in lista2}

        interseccao = lista1_normalizada.intersection(lista2_normalizada)
        uniao = lista1_normalizada.union(lista2_normalizada)

        grau_semelhanca = (len(interseccao) / len(uniao) * 100) if uniao else 0
        return round(grau_semelhanca, 2)

    def getAcuracia(self):
        vp_fn_ratio = (self.VP / (self.VP + self.FN) * 100) if (self.VP + self.FN) != 0 else 0
        vn_fp_ratio = (self.VN / (self.VN + self.FP) * 100) if (self.VN + self.FP) != 0 else 0
        acuracia = 0.5 * (vp_fn_ratio + vn_fp_ratio)
        return round(acuracia, 2)

    def getPrecisao(self):
        precisao = (self.VP / (self.VP + self.FP) * 100) if (self.VP + self.FP) != 0 else 0
        return round(precisao, 2)

    def getRecall(self):
        recall = (self.VP / (self.VP + self.FN) * 100) if (self.VP + self.FN) != 0 else 0
        return round(recall, 2)

    def getF1Score(self):
        precisao = self.getPrecisao() / 100  # Convertendo para proporção
        recall = self.getRecall() / 100      # Convertendo para proporção
        f1_score = (2 * precisao * recall) / (precisao + recall) if (precisao + recall) != 0 else 0
        return round(f1_score * 100, 2)  # Convertendo para porcentagem e arredondando
