from Field.placementOfShips import placementOfShips
from Field.playingFiel import playingField


class Player:
    def __init__(self):
        self.field_attack = playingField()
        self.field_pattern = playingField()
        self.count_cell = 20
        self.placementOfShips = placementOfShips(self.field_pattern)

    def __search_around(self, x, y):
        ships_around = []

        def deck_check(_x, _y):
            if 11 > _x > 0 and 11 > _y > 0 and self.field_pattern.get_cell(_x, _y) == 3:
                ships_around.append([_x + 1, _y])

        deck_check(x + 1, y)
        deck_check(x - 1, y)
        deck_check(x, y + 1)
        deck_check(x, y - 1)
        deck_check(x + 1, y + 1)
        deck_check(x + 1, y - 1)
        deck_check(x - 1, y + 1)
        deck_check(x - 1, y - 1)

        return ships_around

    def __removing_dead_ship(self, ship):
        def removing_deck(_x, _y):
            if 11 > _x > 0 and 11 > _y > 0 and [_x, _y] not in ship:
                self.field_attack.set_cell(_x, _y, 2)

        for deck in ship:
            x = deck[0]
            y = deck[1]
            removing_deck(x + 1, y)
            removing_deck(x - 1, y)
            removing_deck(x, y + 1)
            removing_deck(x, y - 1)
            removing_deck(x + 1, y + 1)
            removing_deck(x + 1, y - 1)
            removing_deck(x - 1, y + 1)
            removing_deck(x - 1, y - 1)

    def __ship_search(self, x, y):
        ship = [[x, y]]
        unseen = self.__search_around(x, y)

        while unseen:
            current = unseen.pop()
            ship.append(current)
            neighbors = self.__search_around(current[0], current[1])
            for i in neighbors:
                if i not in ship:
                    unseen.append(i)

        return ship

    def __checking_ship_killed(self, x, y):
        ship = self.__ship_search(x, y)

        if len(ship) != 1:
            for deck in ship:
                if self.field_attack.get_cell(deck[0], deck[1]) != 1:
                    self.field_attack.set_cell(x, y, 1)
                    return

        self.__removing_dead_ship(ship)

    def do_step(self, x, y):
        if self.field_attack.get_cell(x, y) == 0:
            if self.field_pattern.get_cell(x, y) == 3:
                self.count_cell -= 1
                self.__checking_ship_killed(x, y)
                return 1

            self.field_attack.set_cell(x, y, 2)
            return -1

        else:
            return 'ошибка ввода'  # думаю, что потом эта проверка не понадобится (мы просто оставим кликабельными только доступные клетки

    def end_of_placement(self):
        return self.placementOfShips.end_of_placement()

    def put_ship(self, i, j):
        self.placementOfShips.put_ship(i, j)