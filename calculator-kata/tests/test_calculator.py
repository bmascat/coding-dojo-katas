from src.calculator import StringCalculator

def test_add():
    numbers = "1,2,3"
    calc = StringCalculator()
    result = calc.add(numbers)
    assert result == 6
