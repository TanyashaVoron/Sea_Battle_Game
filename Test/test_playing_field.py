import unittest

from Field.PlayingField import playingField


class TestPlayingField(unittest.TestCase):
    def setUp(self):
        self.field = playingField(3)

    def test_initialization(self):
        self.assertEqual(self.field.get_cell(0, 0), '*')
        self.assertEqual(self.field.get_cell(1, 0), 1)
        self.assertEqual(self.field.get_cell(0, 1), 'A')
        self.assertEqual(self.field.get_cell(3, 3), '0')

    def test_set_get_cell(self):
        self.field.set_cell(1, 1, 'X')
        self.assertEqual(self.field.get_cell(1, 1), 'X')

    def test_convert_to_str(self):
        expected = '* A B C 1 0 0 0 2 0 0 0 3 0 0 0'
        self.assertEqual(self.field.convert_to_str(), expected)

    def test_restoration(self):
        field_str = '* A B C D\n1 0 0 0 0\n2 0 X 0 0\n3 0 0 0 0\n4 0 0 0 0'
        self.field.restoration(field_str)
        self.assertEqual(self.field.get_cell(2, 1), '0')