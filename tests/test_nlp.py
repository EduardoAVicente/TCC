import sys
sys.path.append(".")

from src.controller.nlp_tools.compare_lists import compare_lists
from src.controller.nlp_tools.nltk_compare import similaridadeNLTK
from src.controller.nlp_tools.smith_waterman import smith_waterman
from src.controller.nlp_tools.SpaCy import compare_lists_spacy
from src.controller.nlp_tools.Word2Vec import Word2Vec

def test_compare_lists():
    result = compare_lists(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"], threshold=0.8)
    assert set(result) == {'carro', 'casa', 'moto'}
    
    result = compare_lists(["casa", "carro", "moto"], ["CASA", "CARRO", "AVIÃO"], threshold=0.8)
    assert set(result) == {'carro', 'casa'}
    
    result = compare_lists(["casa", "carro", "moto"], [], threshold=0.8)
    assert result is None
    
    result = compare_lists(["casa", "carro", "moto"], ["jygyg","iggigh","jgjhgjhgjhg"], threshold=0.8)
    assert result is None

def test_similaridadeNLTK():
    result = similaridadeNLTK(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"], threshold=0.8)
    assert set(result) == {'carro', 'casa', 'moto'}
    
    result = similaridadeNLTK(["casa", "carro", "moto"], ["CASA", "CARRO", "AVIÃO"], threshold=0.8)
    assert set(result) == {'carro', 'casa'}
    
    result = similaridadeNLTK(["casa", "carro", "moto"], [], threshold=0.8)
    assert result is None
    
    result = similaridadeNLTK(["casa", "carro", "moto"], ["jygyg","iggigh","jgjhgjhgjhg"], threshold=0.8)
    assert result is None

def test_smith_waterman():
    result = smith_waterman(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"], match=2, mismatch=-1, gap=-1)
    assert set(result) == {'carro', 'casa', 'moto'}
    
    result = smith_waterman(["casa", "carro", "moto"], ["CASA", "CARRO", "AVIÃO"], match=2, mismatch=-1, gap=-1)
    assert set(result) == {'carro', 'casa'}
    
    result = smith_waterman(["casa", "carro", "moto"], [], match=2, mismatch=-1, gap=-1)
    assert result is None
    
    result = smith_waterman(["casa", "carro", "moto"], ["jygyg","iggigh","jgjhgjhgjhg"], match=2, mismatch=-1, gap=-1)
    assert result is None
    
    
def test_compare_lists_spacy():
    result = compare_lists_spacy(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"], threshold=0.8)
    assert set(result) == {'carro', 'casa', 'moto'}
    
    result = compare_lists_spacy(["casa", "carro", "moto"], ["CASA", "CARRO", "AVIÃO"], threshold=0.8)
    assert set(result) == {'carro', 'casa'}
    
    result = compare_lists_spacy(["casa", "carro", "moto"], [], threshold=0.8)
    assert result is None
    
    result = compare_lists_spacy(["casa", "carro", "moto"], ["jygyg","iggigh","jgjhgjhgjhg"], threshold=0.8)
    assert result is None
    
# def test_Word2Vec():
#     result = Word2Vec(["casa", "carro", "moto"], ["CASA", "CARRO", "MOTO"])
#     assert set(result) == {'carro', 'casa', 'moto'}
    
#     result = Word2Vec(["casa", "carro", "moto"], ["CASA", "CARRO", "AVIÃO"])
#     assert set(result) == {'carro', 'casa'}
    
#     result = Word2Vec(["casa", "carro", "moto"], [])
#     assert result is None
    
#     result = Word2Vec(["casa", "carro", "moto"], ["jygyg","iggigh","jgjhgjhgjhg"])
#     assert result is None