class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result: list[str] = []

        for number in range(1, n + 1):
            if number % 15 == 0:
                result.append("FizzBuzz")
            elif number % 3 == 0:
                result.append("Fizz")
            elif number % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(number))

        return result
