import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def similaridadeNLTK(lista1, lista2, threshold=0.8):
    # Baixando os recursos necessários do NLTK (garantindo que só é executado uma vez)
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
    except Exception as e:
        print("Erro ao baixar recursos:", e)

    def palavras_semelhantes(lista1, lista2):
        stop_words = set(stopwords.words('portuguese'))

        def jaccard_similarity(list1, list2):
            set1 = set(list1)
            set2 = set(list2)
            intersection = set1.intersection(set2)
            union = set1.union(set2)
            return len(intersection) / len(union) if union else 0

        palavras_similares = set()

        for frase1 in lista1:
            for frase2 in lista2:
                # Tokenização e conversão para minúsculas
                tokens1 = [word.lower() for word in word_tokenize(frase1) if word.lower() not in stop_words]
                tokens2 = [word.lower() for word in word_tokenize(frase2) if word.lower() not in stop_words]
                similaridade = jaccard_similarity(tokens1, tokens2)
                if similaridade >= threshold:
                    palavras_similares.update(set(tokens1).intersection(tokens2))

        return list(palavras_similares)

    similares = palavras_semelhantes(lista1, lista2)
    return similares if similares else None
