import unittest

from Handler.Parse import Parse


class TestParse(unittest.TestCase):
    def setUp(self):
        self.parser = Parse()

    def test_parse_invalid_turn(self):
        result = self.parser.parse('A', 'A')
        self.assertEqual(result, (0, 0))

    def test_parse_valid_turn_two_digits(self):
        result = self.parser.parse('12B', 10)
        self.assertEqual(result, (0, 0))

    def test_parse_valid_turn_three_digits(self):
        result = self.parser.parse('1A2', 10)
        self.assertEqual(result, (0, 0))

    def test_parse_invalid_x(self):
        result = self.parser.parse('5A', 10)
        self.assertEqual(result, (5, 1))

    def test_parse_invalid_y(self):
        result = self.parser.parse('1K', 10)
        self.assertEqual(result, (0, 0))