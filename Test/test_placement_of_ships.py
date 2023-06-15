import unittest

from Field.PlacementOfStraightShips import placementOfStraightShips
from Field.PlayingField import playingField


class TestPlacementOfStraightShips(unittest.TestCase):
    def test_init_10(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)
        self.assertEqual(placement.array_of_ships, [4, 3, 3, 2, 2, 2, 1, 1, 1, 1])

    def test_init_15(self):
        field = playingField(15)
        placement = placementOfStraightShips(field, 15)
        self.assertEqual(placement.array_of_ships, [5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1])

    def test_init_20(self):
        field = playingField(20)
        placement = placementOfStraightShips(field, 20)
        self.assertEqual(placement.array_of_ships, [6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1])

    def test_get_and_set_cell(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)
        placement.set_cell(0, 0, 'X')
        self.assertEqual(placement.get_cell(0, 0), 'X')

    def test_end_of_placement(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)
        self.assertFalse(placement.end_of_placement())
        placement.cur_ship_index = 10
        self.assertTrue(placement.end_of_placement())

    def test_put_ship(self):
        field = playingField(10)
        field.field = [
            ['*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            ['1', '3', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
            ['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['3', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['4', '3', '3', '3', '3', '3', '3', '0', '0', '0', '0'],
            ['5', '0', '0', '0', '0', '3', '0', '0', '0', '0', '0'],
            ['6', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['7', '0', '0', '0', '0', '0', '2', '2', '2', '2', '0'],
            ['8', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['9', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        ]
        placement = placementOfStraightShips(field, 10)

        placement.put_ship(0, 0)
        self.assertEqual(placement.get_cell(0, 0), '*')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(1, 1)
        self.assertEqual(placement.get_cell(1, 1), '3')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(5, 5)
        self.assertEqual(placement.get_cell(5, 5), '3')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(5, 6)
        self.assertEqual(placement.get_cell(5, 6), '3')
        self.assertEqual(placement.cur_state, 1)

        placement.put_ship(5, 7)
        self.assertEqual(placement.get_cell(5, 7), '3')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(5, 8)
        self.assertEqual(placement.get_cell(5, 8), '3')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(5, 9)
        self.assertEqual(placement.get_cell(5, 9), '3')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(5, 9)
        self.assertEqual(placement.get_cell(8, 10), '0')
        self.assertEqual(placement.cur_state, 0)

        placement.put_ship(5, 9)
        self.assertEqual(placement.get_cell(7, 9), '2')
        self.assertEqual(placement.cur_state, 0)

    def test_checking_the_correct_direction(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)

        placement.get_cell(4, 2)
        placement.show_free_directions(4, 2, 3)
        self.assertTrue(placement.checking_the_correct_direction(4, 3))

        placement.get_cell(5, 3)
        placement.show_free_directions(5, 3, 3)
        self.assertTrue(placement.checking_the_correct_direction(5, 2))

        placement.get_cell(7, 2)
        placement.show_free_directions(7, 2, 3)
        self.assertTrue(placement.checking_the_correct_direction(8, 2))

        placement.get_cell(9, 5)
        placement.show_free_directions(9, 5, 3)
        self.assertTrue(placement.checking_the_correct_direction(8, 5))

    def test_show_free_directions(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)

        placement.get_cell(4, 4)
        placement.show_free_directions(4, 4, 2)
        self.assertEqual(placement.get_cell(4, 3), "?")
        self.assertEqual(placement.get_cell(4, 5), "?")
        self.assertEqual(placement.get_cell(3, 4), "?")
        self.assertEqual(placement.get_cell(5, 4), "?")

    def test_remove_question_marks(self):
        field = playingField(10)
        field.field = [
            ['*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            ['1', '3', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
            ['2', '0', '?', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['3', '0', '?', '?', '?', '?', '?', '?', '?', '0', '0'],
            ['4', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['5', '0', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['6', '0', '?', '?', '?', '?', '?', '?', '?', '0', '0'],
            ['7', '0', '?', '?', '?', '?', '2', '2', '2', '2', '0'],
            ['8', '0', '?', '?', '?', '?', '?', '?', '?', '0', '0'],
            ['9', '0', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        ]
        placement = placementOfStraightShips(field, 10)
        placement.remove_question_marks()
        for i in range(1, field.n):
            for j in range(1, field.n):
                self.assertNotEqual(placement.get_cell(i, j), "?")

    def test_remove_exclamation_marks(self):
        field = playingField(10)
        field.field = [
            ['*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            ['1', '3', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
            ['2', '0', '?', '0', '0', '0', '!', '!', '!', '?', '?'],
            ['3', '0', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['4', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['5', '0', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['6', '0', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['7', '0', '?', '?', '?', '?', '2', '2', '2', '2', '?'],
            ['8', '0', '?', '?', '?', '?', '!', '!', '!', '?', '?'],
            ['9', '0', '?', '?', '?', '?', '!', '!', '!', '!', '!'],
            ['10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        ]
        placement = placementOfStraightShips(field, 10)
        placement.remove_exclamation_marks()
        for i in range(1, field.n):
            for j in range(1, field.n):
                self.assertNotEqual(placement.get_cell(i, j), "!")

    def test_check_free_direction(self):
        field = playingField(10)
        field.field = [
            ['*', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            ['1', '3', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
            ['2', '0', '?', '0', '0', '0', '!', '!', '!', '?', '?'],
            ['3', '0', '?', '?', '?', '?', '?', '?', '?', '?', '?'],
            ['4', '?', '?', '?', '?', '?', '0', '?', '?', '?', '?'],
            ['5', '0', '?', '?', '?', '?', '0', '?', '?', '?', '?'],
            ['6', '0', '?', '?', '?', '?', '0', '?', '?', '?', '?'],
            ['7', '0', '?', '?', '?', '?', '0', '2', '2', '2', '?'],
            ['8', '0', '?', '?', '?', '?', '!', '!', '!', '?', '?'],
            ['9', '0', '?', '?', '?', '?', '!', '!', '!', '!', '!'],
            ['10', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
        ]
        placement = placementOfStraightShips(field, 10)
        self.assertTrue(placement.check_free_direction(7, 6, "up"))
        self.assertFalse(placement.check_free_direction(7, 6, "down"))
        self.assertFalse(placement.check_free_direction(7, 6, "left"))
        self.assertFalse(placement.check_free_direction(7, 6, "right"))

    def test_fence_off_ship(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)
        placement.cur_ship_index = 4
        placement.last_cell = [4, 4]
        placement.fence_off_ship("up")
        for i in range(2, 6):
            for j in range(3, 6):
                self.assertEqual(placement.get_cell(i, j), "!")

    def test_fence_off_cell(self):
        field = playingField(10)
        placement = placementOfStraightShips(field, 10)
        placement.fence_off_cell(7, 7)
        surrounding_cells = [[6, 6], [6, 7], [6, 8], [7, 6], [7, 8], [8, 6], [8, 7], [8, 8]]
        for cell in surrounding_cells:
            self.assertEqual(placement.get_cell(cell[0], cell[1]), "!")
