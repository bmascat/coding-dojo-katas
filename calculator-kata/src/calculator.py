class StringCalculator:
    def add(self, numbers: str) -> int:
        return sum(int(number) for number in numbers.split(","))

