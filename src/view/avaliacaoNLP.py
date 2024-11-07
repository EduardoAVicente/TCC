import numpy as np
import matplotlib.pyplot as plt
from controller.nlp_tools.compare_lists import compare_lists
from controller.nlp_tools.nltk_compare import similaridadeNLTK
from controller.nlp_tools.smith_waterman import smith_waterman
from controller.nlp_tools.SpaCy import compare_lists_spacy
from controller.nlp_tools.Word2Vec import Word2Vec
from controller.avaliacaoNLP import avaliacaoNLPController

class AvaliacaoNLP:   
    def main(self):    
        algoritmos = [
            ("Compare Lists", compare_lists),
            ("Similaridade NLTK", similaridadeNLTK),
            ("Smith-Waterman", smith_waterman),
            ("SpaCy", compare_lists_spacy),
            ("Word2Vec", Word2Vec)
        ]
        
        avaliacaoNLP = avaliacaoNLPController(algoritmos)
        print(avaliacaoNLP.main())


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

