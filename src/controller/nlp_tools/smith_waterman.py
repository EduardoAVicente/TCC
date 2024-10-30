import numpy as np

def smith_waterman(list1, list2, match=2, mismatch=-1, gap=-1):
    # Converter ambas as listas para minúsculas para ignorar a diferença entre maiúsculas e minúsculas
    list1 = [item.lower() for item in list1]
    list2 = [item.lower() for item in list2]
    
    len1, len2 = len(list1), len(list2)
    
    # Criação da matriz de pontuação
    score_matrix = np.zeros((len1 + 1, len2 + 1))

    max_score = 0
    max_pos = None

    # Preenchimento da matriz de pontuação
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if list1[i - 1] == list2[j - 1]:
                score = match
            else:
                score = mismatch

            score_matrix[i][j] = max(0,
                                     score_matrix[i - 1][j - 1] + score,  # Match/Mismatch
                                     score_matrix[i - 1][j] + gap,         # Deletion
                                     score_matrix[i][j - 1] + gap)         # Insertion
            
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

    # Verificar se alguma correspondência foi encontrada
    if max_pos is None:
        return None  # Retorna None se não houver correspondência

    # Traçar o alinhamento e coletar as palavras semelhantes
    similar_words = []
    i, j = max_pos

    while score_matrix[i][j] != 0:
        if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match if list1[i - 1] == list2[j - 1] else mismatch):
            similar_words.append(list1[i - 1])  # Adiciona a palavra semelhante
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + gap:
            i -= 1
        else:
            j -= 1

    return list(reversed(similar_words)) if similar_words else None  # Retorna None se a lista estiver vazia
