from Field.PlacementOfAngularShips import placementOfAngularShips
from Field.PlacementOfStraightShips import placementOfStraightShips
from Field.PlayingField import playingField


class Player:
    def __init__(self, field_size, placement_ships):
        self.field_size = int(field_size)
        self.field_attack = playingField(field_size)
        self.field_pattern = playingField(field_size)
        self.count_cell = self.__calculate_count_cell__()
        if placement_ships == 0:
            self.placement_of_ships = placementOfStraightShips(self.field_pattern, self.field_size)
        else:
            self.placement_of_ships = placementOfAngularShips(self.field_pattern, self.field_size)
    def set_field_size(self, size):
        self.field_size = size
        self.__calculate_count_cell__()
    def __calculate_count_cell__(self):
        count_cell = {10: 20, 15: 35, 20: 56}
        return count_cell[self.field_size]

    # поиск палуб кораблей вокруг
    def __search_around__(self, x, y):
        ships_around = []

        def __deck_check__(_x, _y):
            if self.field_size >= _x > 0 and self.field_size >= _y > 0 and self.field_pattern.get_cell(_x, _y) == '3':
                ships_around.append([_x, _y])  #

        __deck_check__(x + 1, y)
        __deck_check__(x - 1, y)
        __deck_check__(x, y + 1)
        __deck_check__(x, y - 1)
        __deck_check__(x + 1, y + 1)
        __deck_check__(x + 1, y - 1)
        __deck_check__(x - 1, y + 1)
        __deck_check__(x - 1, y - 1)

        return ships_around

    # удаление из игры полей вокруг коробля
    def __removing_dead_ship__(self, ship):
        def __removing_deck__(_x, _y):
            if self.field_size >= _x > 0 and self.field_size >= _y > 0 and [_x, _y] not in ship:
                self.field_attack.set_cell(_x, _y, '2')

        for deck in ship:
            x = deck[0]
            y = deck[1]
            __removing_deck__(x + 1, y)
            __removing_deck__(x - 1, y)
            __removing_deck__(x, y + 1)
            __removing_deck__(x, y - 1)
            __removing_deck__(x + 1, y + 1)
            __removing_deck__(x + 1, y - 1)
            __removing_deck__(x - 1, y + 1)
            __removing_deck__(x - 1, y - 1)

    # поиск целого корабля по одной палубе
    def __ship_search__(self, x, y):
        ship = [[x, y]]
        unseen = self.__search_around__(x, y)

        while unseen:
            current = unseen.pop()
            ship.append(current)
            neighbors = self.__search_around__(current[0], current[1])
            for i in neighbors:
                if i not in ship:
                    unseen.append(i)

        return ship

    # проверка на то, что корабль выбит целиком
    def __checking_ship_killed__(self, x, y):
        ship = self.__ship_search__(x, y)
        print(x, y, ship)
        if len(ship) != 1:
            for deck in ship:
                if self.field_attack.get_cell(deck[0], deck[1]) != '1':
                    self.field_attack.set_cell(x, y, '1')
                    return

        self.__removing_dead_ship__(ship)

    # основной метод: сделать ход
    def do_step(self, x, y):
        if self.field_attack.get_cell(x, y) == '0':
            if self.field_pattern.get_cell(x, y) == '3':
                self.field_attack.set_cell(x, y, '1')
                self.count_cell -= 1
                self.__checking_ship_killed__(x, y)
                return 1

            self.field_attack.set_cell(x, y, '2')
            return -1

        else:
            return 0

    def end_of_placement(self):
        if self.placement_of_ships.end_of_placement():
            return True
        return False

    def put_ship(self, x, y):
        self.placement_of_ships.put_ship(x, y)

    def show_field_pattern(self):
        return self.field_pattern

    def show_field_attack(self):
        return self.field_attack
