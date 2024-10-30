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
                # Armazenando as palavras em maiúsculas e minúsculas, se forem semelhantes
                if similaridade > 0:  # Ajuste o limiar de similaridade conforme necessário
                    resultados.append((palavra1.lower(), palavra2.lower(), similaridade))
                    resultados.append((palavra1.upper(), palavra2.upper(), similaridade))
            else:
                resultados.append((palavra1, palavra2, "Não encontrado no vocabulário"))
    
    # Filtrando palavras semelhantes
    palavras_semelhantes = [(p1, p2, sim) for p1, p2, sim in resultados if isinstance(sim, float) and sim > 0.5]  # Limiar de similaridade
    
    return palavras_semelhantes

