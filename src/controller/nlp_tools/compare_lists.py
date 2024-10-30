from Bio import Align

def compare_lists(list1, list2):
    # Verificando se as listas não são None
    if list1 is None or list2 is None:
        raise ValueError("Uma das listas está vazia (None). Certifique-se de que ambas as listas sejam válidas.")

    similar_words = []
    aligner = Align.PairwiseAligner()  # Novo alinhador
    aligner.mode = 'local'  # Modo local, como o Smith-Waterman
    
    for word1 in list1:
        for word2 in list2:
            # Usando o PairwiseAligner para comparar as palavras
            score = aligner.score(word1, word2)  # Obtendo a pontuação de similaridade
            
            # Definindo um limite de similaridade para considerar as palavras similares
            if score > 0.8 * len(word1):  # Exemplo de threshold
                similar_words.append((word1, word2, score))
    
    return similar_words