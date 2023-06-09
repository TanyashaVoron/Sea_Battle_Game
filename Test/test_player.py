import unittest

from Field.PlayingField import playingField
from Player.Player import Player


class TestPlayer(unittest.TestCase):
    def test_end_of_placement(self):
        player = Player(10, 0)
        self.assertEqual(player.end_of_placement(), False)

    def test_put_ship(self):
        player = Player(10, 0)
        player.put_ship(1, 1)
        self.assertEqual(player.field_pattern.get_cell(1, 1), '3')

    def test_show_field_pattern(self):
        player = Player(10, 0)
        self.assertIsInstance(player.show_field_pattern(), playingField)

    def test_show_field_attack(self):
        player = Player(10, 0)
        self.assertIsInstance(player.show_field_attack(), playingField)

    def test_do_step(self):
        player = Player(10, 0)
        player.put_ship(1, 1)
        self.assertEqual(player.do_step(1, 1), 1)

    def test_calculate_count_cell(self):
        player = Player(10, 0)
        self.assertEqual(player.__calculate_count_cell__(), 20)

    def test_search_around(self):
        player = Player(10, 0)
        player.put_ship(2, 2)
        self.assertEqual(player.__search_around__(2, 2), [[2, 2]])

    def test_removing_dead_ship(self):
        player = Player(10, 0)
        player.put_ship(2, 2)
        player.do_step(2, 2)
        self.assertEqual(player.field_attack.get_cell(2, 2), '1')
        self.assertEqual(player.field_attack.get_cell(2, 3), '2')
        self.assertEqual(player.field_attack.get_cell(3, 2), '2')
        self.assertEqual(player.field_attack.get_cell(3, 3), '2')

    def test_ship_search(self):
        player = Player(10, 0)
        player.put_ship(2, 2)
        self.assertEqual(player.__ship_search__(2, 2), [[2, 2], [2, 2]])

    def test_checking_ship_killed(self):
        player = Player(10, 0)
        player.put_ship(2, 2)
        player.do_step(2, 2)
        self.assertEqual(player.field_attack.get_cell(2, 2), '1')
        self.assertEqual(player.field_attack.get_cell(2, 3), '2')