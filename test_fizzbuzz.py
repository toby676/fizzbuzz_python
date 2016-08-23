import unittest
from lib import fizzbuzz
FizzBuzz = fizzbuzz.FizzBuzz()

class FizzBuzzTest(unittest.TestCase):
    def test_1_returns_1(self):
        self.assertEqual(FizzBuzz.play(1), 1)

    def test_3_returns_fizz(self):
        self.assertEqual(FizzBuzz.play(3), "Fizz")

if __name__ == '__main__':
	unittest.main()
