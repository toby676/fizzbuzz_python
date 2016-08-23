import unittest
from lib import fizzbuzz
FizzBuzz = fizzbuzz.FizzBuzz()

class FizzBuzzTest(unittest.TestCase):
    def test_1_returns_1(self):
        self.assertEqual(FizzBuzz.play(1), 1)

    def test_3_returns_fizz(self):
        self.assertEqual(FizzBuzz.play(3), "Fizz")

    def test_5_returns_buzz(self):
        self.assertEqual(FizzBuzz.play(5), "Buzz")

    def test_15_returns_fizzbuzz(self):
        self.assertEqual(FizzBuzz.play(15), "FizzBuzz")

if __name__ == '__main__':
	unittest.main()
