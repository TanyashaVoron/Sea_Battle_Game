import unittest
from Player.BotPlayer import Bot


class TestBot(unittest.TestCase):
    def test_bot_generation_move(self):
        bot = Bot(10, 0)
        move = bot.bot_generation_move()
        self.assertIsInstance(move, str)
        self.assertRegex(move, r'^[1-9][0-9]?[A-Z]$')

    def test_bot_generation_rational_move(self):
        bot = Bot(10, 0)
        bot.last_move_x, bot.last_move_y = 5, 5
        bot.field_pattern.set_cell(4, 4, '3')
        bot.field_attack.set_cell(4, 4, '1')
        bot.field_pattern.set_cell(4, 5, '3')
        bot.field_attack.set_cell(4, 5, '1')
        bot.field_pattern.set_cell(4, 6, '3')
        bot.field_attack.set_cell(4, 6, '1')
        bot.field_pattern.set_cell(5, 4, '3')
        bot.field_attack.set_cell(5, 4, '1')
        bot.field_pattern.set_cell(5, 6, '3')
        bot.field_attack.set_cell(5, 6, '1')
        bot.field_pattern.set_cell(6, 4, '3')
        bot.field_attack.set_cell(6, 4, '1')
        bot.field_pattern.set_cell(6, 5, '3')
        bot.field_attack.set_cell(6, 5, '1')
        bot.field_pattern.set_cell(6, 6, '3')
        bot.field_attack.set_cell(6, 6, '1')

        move = bot.bot_generation_rational_move()
        self.assertIsInstance(move, str)
        self.assertRegex(move, r'^[1-9][0-9]?[A-Z]$')


