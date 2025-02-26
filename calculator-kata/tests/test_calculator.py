from src.calculator import Calculator

def test_add():
    numbers = "1,2,3"
    calc = Calculator()
    result = calc.add(numbers)
    assert result == 6
