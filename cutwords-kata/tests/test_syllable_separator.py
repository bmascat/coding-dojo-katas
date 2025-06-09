import pytest
from src.syllable_separator import SyllableSeparator

@pytest.fixture(scope="module")
def syllable_separator():
    return SyllableSeparator()

