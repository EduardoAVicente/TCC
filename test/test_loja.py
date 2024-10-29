# test_teste2.py
import pytest
from teste2 import seila

@pytest.fixture
def test_seila():
    assert seila() == 2
