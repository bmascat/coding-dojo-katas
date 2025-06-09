import pytest
from src.syllable_separator import SyllableSeparator

import pytest
from src.syllable_separator import SyllableSeparator

@pytest.fixture
def separator():
    return SyllableSeparator()

def test_simple_word(separator):
    assert separator.separate("maraca") == ["ma", "ra", "ca"]
    assert separator.separate("tijera") == ["ti", "je", "ra"]

def test_double_consonant(separator):
    assert separator.separate("chilla") == ["chi", "lla"]
    assert separator.separate("chorro") == ["cho", "rro"]

def test_two_consonants_between_two_vowels(separator):
    assert separator.separate("campo") == ["cam", "po"]
    assert separator.separate("salto") == ["sal", "to"]
    assert separator.separate("harto") == ["har", "to"]
    assert separator.separate("ando") == ["an", "do"]