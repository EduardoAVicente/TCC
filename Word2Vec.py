import gensim.downloader as api

def Word2Vec(lista1, lista2):
    # Carregando o modelo pré-treinado Word2Vec
    model = api.load("word2vec-google-news-300")

    resultados = []
    
    # Percorrendo todas as combinações de palavras entre as duas listas
    for palavra1 in lista1:
        for palavra2 in lista2:
            # Verificando se ambas as palavras estão no vocabulário do modelo
            if palavra1 in model.key_to_index and palavra2 in model.key_to_index:
                # Calculando a similaridade entre as duas palavras
                similaridade = model.similarity(palavra1, palavra2)
                resultados.append((palavra1, palavra2, similaridade))
            else:
                resultados.append((palavra1, palavra2, "Não encontrado no vocabulário"))
    
    return resultados