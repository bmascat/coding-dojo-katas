import pytest
from src.parser_arguments import ParserArguments

@pytest.fixture(scope="module")
def parser():
    return ParserArguments()

def test_instance_of_parser_arguments(parser):
    assert isinstance(parser, ParserArguments)
