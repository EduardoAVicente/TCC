import numpy as np
import matplotlib.pyplot as plt
import time  # Adicione esta linha
from tabulate import tabulate
from controller.nlp_tools.compare_lists import compare_lists
from controller.nlp_tools.nltk_compare import similaridadeNLTK
from controller.nlp_tools.smith_waterman import smith_waterman
from controller.nlp_tools.SpaCy import compare_lists_spacy
from controller.nlp_tools.Word2Vec import Word2Vec
from model.avaliacaoNLP import testes

class AvaliacaoNLP:   
    def main(self):    
        num_testes = len(testes)
        algoritmos = [
            ("Compare Lists", compare_lists),
            ("Similaridade NLTK", similaridadeNLTK),
            ("Smith-Waterman", smith_waterman),
            # ("SpaCy", compare_lists_spacy),
            # ("Word2Vec", Word2Vec)
        ]
        
        # Estruturas para armazenar resultados
        resultados = {alg[0]: ["semelhanca"] + [0] * num_testes for alg in algoritmos}
        tempos = {alg[0]: ["tempo"] + [0] * num_testes for alg in algoritmos}  # Use 0 para os tempos

        for i in range(num_testes):
            for algoritmo_nome, algoritmo_func in algoritmos:
                start_time = time.time()
                resultado = algoritmo_func(testes[i][0], testes[i][1])  # teste[numero do teste][elemento do teste]
                end_time = time.time()
                elapsed_time = round(end_time - start_time, 4) * 1000  # converter para milissegundos
                
                if resultado is None or len(resultado) == 0:
                    resultados[algoritmo_nome][i + 1] = 0  # Definir como 0 se falhar
                else:
                    similaridade = self.calcular_semelhanca(resultado, testes[i][2])
                    resultados[algoritmo_nome][i + 1] = similaridade
                
                # Armazenar tempos
                tempos[algoritmo_nome][i + 1] = elapsed_time  # Armazenar como número float

        # Calcular as médias
        medias_sim = {alg[0]: round(sum(resultados[alg[0]][1:]) / num_testes, 2) for alg in algoritmos}
        medias_tempo = {alg[0]: round(sum(tempos[alg[0]][1:]) / num_testes, 2) for alg in algoritmos}

        # Imprimir a tabela no formato desejado
        print(self.tabela(resultados, tempos, medias_sim, medias_tempo, num_testes))
        
        # Corrigir conversão de tempos para float, removendo o "ms"
        tempos_float = {alg[0]: tempos[alg[0]][1:] for alg in algoritmos}  # Agora é uma lista de floats
        # Gerar gráfico comparativo para todos os algoritmos
        self.gerar_grafico(resultados, tempos_float, num_testes, algoritmos)

    def calcular_semelhanca(self, lista1, lista2):
        lista1_normalizada = {item.strip().lower() for item in lista1}
        lista2_normalizada = {item.strip().lower() for item in lista2}

        interseccao = lista1_normalizada.intersection(lista2_normalizada)
        uniao = lista1_normalizada.union(lista2_normalizada)

        grau_semelhanca = (len(interseccao) / len(uniao) * 100) if uniao else 0
        grau_semelhanca = round(grau_semelhanca, 2)

        return grau_semelhanca

    def tabela(self, resultados, tempos, medias_sim, medias_tempo, quant_testes):
        # Criar a tabela conforme o formato desejado
        headers = ["Algoritmo", "Metricas"] + [f"Teste {i+1}" for i in range(quant_testes)] + ["Média"]
        dados = []
        
        for algoritmo_nome in resultados.keys():
            dados.append([algoritmo_nome, "semelhanca"] + resultados[algoritmo_nome][1:] + [medias_sim[algoritmo_nome]])
            dados.append(["", "tempo"] + [f"{tempo:.2f}ms" for tempo in tempos[algoritmo_nome][1:]] + [f"{medias_tempo[algoritmo_nome]:.2f}ms"])
        
        return tabulate(dados, headers=headers, tablefmt='grid')

    def gerar_grafico(self, resultados, tempos, num_testes, algoritmos):
        testes = [f'Teste {i + 1}' for i in range(num_testes)]
        x = np.arange(num_testes)  # Posições no eixo x

        # Configuração do gráfico
        fig, ax1 = plt.subplots(figsize=(12, 6))

        # Gráfico de barras para similaridade
        largura = 0.35  # Largura das barras
        for idx, algoritmo_nome in enumerate(resultados.keys()):
            similaridades = resultados[algoritmo_nome][1:]
            ax1.bar(x + (idx * largura), similaridades, largura, label=algoritmo_nome)

        ax1.set_xlabel('Testes')
        ax1.set_ylabel('Semelhanca (%)', color='tab:blue')
        ax1.tick_params(axis='y', labelcolor='tab:blue')
        ax1.set_xticks(x + (len(algoritmos) - 1) * largura / 2)
        ax1.set_xticklabels(testes)

        # Gráfico de linha para tempo
        ax2 = ax1.twinx()  
        for algoritmo_nome in algoritmos:
            tempos_alg = tempos[algoritmo_nome[0]]
            # Verifica se a lista de tempos tem o mesmo tamanho que testes
            if len(tempos_alg[1:]) == num_testes:
                ax2.plot(testes, tempos_alg[1:], marker='o', label=f'Tempo {algoritmo_nome[0]}')

        ax2.set_ylabel('Tempo (ms)', color='tab:red')
        ax2.tick_params(axis='y', labelcolor='tab:red')

        # Adicionando título e legendas
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')
        plt.title('Comparação de Semelhanca e Tempo por Algoritmo e Teste')
        plt.tight_layout()  
        plt.show()

