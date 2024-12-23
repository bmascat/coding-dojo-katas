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

def test_default_bool_value(parser):
    list_args = parser.parse("-p value -r 1")
    assert isinstance(list_args["q"], parser.schema["q"])
    assert list_args["q"] is False

def test_default_int_value(parser):
    list_args = parser.parse("-p value -q")
    assert isinstance(list_args["r"], parser.schema["r"])
    assert list_args["r"] == 0

def test_default_str_value(parser):
    list_args = parser.parse("-q -r 1")
    assert isinstance(list_args["p"], parser.schema["p"])
    assert list_args["p"] == ""



