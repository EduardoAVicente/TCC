from controller.nlp_tools.compare_lists import compare_lists
from controller.nlp_tools.nltk_compare import similaridadeNLTK
from controller.nlp_tools.smith_waterman import smith_waterman
from controller.nlp_tools.SpaCy import compare_lists_spacy
from controller.nlp_tools.Word2Vec import Word2Vec

class AvaliacaoNLP:
    def main():
        # print(compare_lists(["casa", "carro", "moto"], ["BATTA", "DSFSDF", "SDF"]))
        
        # print(similaridadeNLTK(["casa", "carro", "moto"], ["casa", "carro", "moto"]))
        
        # print(smith_waterman(["casa", "carro", "moto"], ["BATTA", "DSFSDF", "SDF"]))
        # print(smith_waterman(["casa", "carro", "moto"], []))
        # print(smith_waterman(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"], match=2, mismatch=-1, gap=-1))
        
        
        # print(compare_lists_spacy(["casa", "carro", "moto"], ["BATTA", "DSFSDF", "SDF"]))
        # print(compare_lists_spacy(["casa", "carro", "moto"], []))
        # print(compare_lists_spacy(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"]))
        # print(compare_lists_spacy(["casa", "carro", "moto"], ["casa", "carro", "moto"]))
        
        # print(Word2Vec(["casa", "carro", "moto"], ["BATTA", "DSFSDF", "SDF"]))
        # print(Word2Vec(["casa", "carro", "moto"], []))
        # print(Word2Vec(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"]))
        # print(Word2Vec(["casa", "carro", "moto"], ["casa", "carro", "moto"]))        
        # print(Word2Vec(["automobile", "bicycle", "train"], ["car", "bike", "train"]))
        
        
        pass