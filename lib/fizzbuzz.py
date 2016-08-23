class FizzBuzz:
    def play(self, number):
        if number % 3 == 0:
            return 'Fizz'
        if number % 5 == 0:
            return 'Buzz'
        return number
