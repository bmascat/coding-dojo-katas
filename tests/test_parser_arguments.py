import pytest
from src.parser_arguments import ParserArguments

@pytest.fixture(scope="module")
def parser():
    return ParserArguments(schema={
        "p": str,
        "q": bool,
        "r": int,
    })

def test_instance_of_parser_arguments(parser):
    assert isinstance(parser, ParserArguments)

def test_parse_one_argument(parser):
    list_args = parser.parse("-p value")
    assert isinstance(list_args["p"], parser.schema["p"])
    
def test_parse_two_arguments(parser):   
    list_args = parser.parse("-p value -q")
    assert isinstance(list_args["p"], parser.schema["p"])
    assert isinstance(list_args["q"], parser.schema["q"])

def test_parse_three_arguments(parser):
    list_args = parser.parse("-p value -q -r 1")
    assert isinstance(list_args["p"], parser.schema["p"])
    assert isinstance(list_args["q"], parser.schema["q"])
    assert isinstance(list_args["r"], parser.schema["r"])

