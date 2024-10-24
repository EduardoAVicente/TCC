import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Baixando os recursos necessários do NLTK (garantindo que só é executado uma vez)
try:
    nltk.download('punkt_tab', quiet=True)
    nltk.download('stopwords', quiet=True)
except Exception as e:
    print("Erro ao baixar recursos:", e)

def frases_semelhantes(lista1, lista2, threshold=0.5):
    stop_words = set(stopwords.words('portuguese'))

    def jaccard_similarity(list1, list2):
        set1 = set(list1)
        set2 = set(list2)
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return len(intersection) / len(union) if union else 0

    frases_semelhantes = set()  # Conjunto para frases semelhantes
    frases_nao_semelhantes = set()  # Conjunto para frases não semelhantes

    for frase1 in lista1:
        frase1_adicionada = False  # Flag para saber se a frase1 foi considerada semelhante
        for frase2 in lista2:
            tokens1 = [word for word in word_tokenize(frase1.lower()) if word not in stop_words]
            tokens2 = [word for word in word_tokenize(frase2.lower()) if word not in stop_words]
            similaridade = jaccard_similarity(tokens1, tokens2)
            if similaridade >= threshold:
                frases_semelhantes.add(frase1)  # Adiciona frase1 se for semelhante a frase2
                frases_semelhantes.add(frase2)  # Adiciona frase2 também
                frase1_adicionada = True  # Marca como semelhante
            else:
                frases_nao_semelhantes.add(frase2)  # Adiciona frase2 como não semelhante

        if not frase1_adicionada:  # Se frase1 não foi semelhante a nenhuma frase2, adiciona como não semelhante
            frases_nao_semelhantes.add(frase1)

    # Combina as frases semelhantes e não semelhantes, sem repetições
    resultado_final = list(frases_semelhantes.union(frases_nao_semelhantes))

    return resultado_final