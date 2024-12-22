import pytest
from src.parser_arguments import ParserArguments

@pytest.fixture(scope="module")
def parser():
    return ParserArguments(schema={
        "p": str,
    })

def test_instance_of_parser_arguments(parser):
    assert isinstance(parser, ParserArguments)

def test_parse_one_argument(parser):
    list_args = parser.parse("-p value")
    assert isinstance(list_args["p"], parser.schema["p"])