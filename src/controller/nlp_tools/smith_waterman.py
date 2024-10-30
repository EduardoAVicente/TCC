import numpy as np

def smith_waterman(seq1, seq2, match=2, mismatch=-1, gap=-1):
    len1, len2 = len(seq1), len(seq2)
    
    # Criação da matriz de pontuação
    score_matrix = np.zeros((len1 + 1, len2 + 1))

    max_score = 0
    max_pos = None

    # Preenchimento da matriz de pontuação
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if seq1[i - 1] == seq2[j - 1]:
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

    # Traçar o alinhamento
    aligned_seq1 = []
    aligned_seq2 = []
    i, j = max_pos

    while score_matrix[i][j] != 0:
        if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i - 1][j - 1] + (match if seq1[i - 1] == seq2[j - 1] else mismatch):
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + gap:
            aligned_seq1.append(seq1[i - 1])
            aligned_seq2.append('-')
            i -= 1
        else:
            aligned_seq1.append('-')
            aligned_seq2.append(seq2[j - 1])
            j -= 1

    return ''.join(reversed(aligned_seq1)), ''.join(reversed(aligned_seq2)), max_score