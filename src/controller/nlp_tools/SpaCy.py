import os
import spacy

# Carregue o modelo de linguagem
# nlp = spacy.load("pt_core_news_sm")

nlp = spacy.load("pt_core_news_md")


def compare_lists(list1, list2):
    similarities = {}
    
    for text1 in list1:
        doc1 = nlp(text1)
        for text2 in list2:
            doc2 = nlp(text2)
            similarity = doc1.similarity(doc2)
            similarities[(text1, text2)] = similarity
            
    return similarities

def save_to_log(similarities):
    # Cria a pasta SpaCy caso não exista
    os.makedirs("SpaCy", exist_ok=True)

    # Gera o nome do arquivo de log
    log_file_path = "SpaCy/SpaCy.log"
    file_index = 1
    
    # Verifica se o arquivo já existe e cria um novo com índice se necessário
    while os.path.exists(log_file_path):
        log_file_path = f"SpaCy/SpaCy{file_index}.log"
        file_index += 1
    
    # Salva as similaridades no arquivo de log
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        for (text1, text2), similarity in similarities.items():
            log_file.write(f"'{text1}' vs '{text2}': {similarity}\n")