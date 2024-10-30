from Bio import Align

def compare_lists(list1, list2, threshold=0.8):
    # Verificando se as listas não são None
    if list1 is None or list2 is None:
        raise ValueError("Uma das listas está vazia (None). Certifique-se de que ambas as listas sejam válidas.")
    
    similar_words = []
    aligner = Align.PairwiseAligner()  # Inicializa o alinhador
    aligner.mode = 'local'  # Define o modo de alinhamento local
    
    for word1 in list1:
        for word2 in list2:
            # Convertendo as palavras para minúsculas para comparação case-insensitive
            score = aligner.score(word1.lower(), word2.lower())  # Calcula a pontuação de similaridade
            
            # Definindo um limite de similaridade baseado no parâmetro threshold
            similarity_threshold = threshold * min(len(word1), len(word2))
            if score >= similarity_threshold:
                similar_words.append(word1)
    
    if not set(similar_words):
        return None
    else:
        return list(set(similar_words))