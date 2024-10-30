import spacy
import warnings

def compare_lists_spacy(list1, list2, threshold=0.8):
    # Ignora avisos de similaridade
    warnings.simplefilter("ignore", category=UserWarning)
    
    # Carregue o modelo de linguagem
    nlp = spacy.load("pt_core_news_lg")

    similar_words = set()  # Usar um conjunto para evitar duplicatas
    
    for text1 in list1:
        text1 = text1.strip()  # Remove espaços em branco no início e no fim
        if not text1:  # Ignora textos vazios
            continue
            
        doc1 = nlp(text1.lower())  # Converte para minúsculas
        if doc1.vector.size == 0:  # Ignora textos com vetores vazios
            continue
            
        for text2 in list2:
            text2 = text2.strip()  # Remove espaços em branco no início e no fim
            if not text2:  # Ignora textos vazios
                continue
                
            doc2 = nlp(text2.lower())  # Converte para minúsculas
            if doc2.vector.size == 0:  # Ignora textos com vetores vazios
                continue

            similarity = doc1.similarity(doc2)
            if similarity > threshold:
                similar_words.add(text1.lower())  # Adiciona apenas a palavra em minúsculas
                similar_words.add(text2.lower())  # Adiciona apenas a palavra em minúsculas
                
    if not list(similar_words):
        return None
    else:
        return list(similar_words)
