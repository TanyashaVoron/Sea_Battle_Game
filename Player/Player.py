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

    def do_step(self, x, y):
        """
        основной метод: сделать ход
        """
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

    def __calculate_count_cell__(self):
        """
        определение количества палуб корабля в зависимости от размера поля
        """
        count_cell = {10: 20, 15: 35, 20: 56}
        return count_cell[self.field_size]

    def __search_around__(self, x, y):
        """
        поиск палуб кораблей вокруг
        """
        ships_around = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                _x, _y = x + i, y + j
                if self.field_size >= _x > 0 and self.field_size >= _y > 0 and self.field_pattern.get_cell(_x,
                                                                                                           _y) == '3':
                    ships_around.append([_x, _y])

        return ships_around

    def __removing_dead_ship__(self, ship):
        """
        Yдаление из игры полей вокруг коробля
        :param ship: все палубы корабля
        """
        for deck in ship:
            x = deck[0]
            y = deck[1]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    _x, _y = x + i, y + j
                    if self.field_size >= _x > 0 and self.field_size >= _y > 0 and [_x, _y] not in ship:
                        self.field_attack.set_cell(_x, _y, '2')

    def __ship_search__(self, x, y):
        """
        поиск целого корабля по одной палубе
        """
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

    def __checking_ship_killed__(self, x, y):
        """
        проверка на то, что корабль выбит целиком
        """
        ship = self.__ship_search__(x, y)
        if len(ship) != 1:
            for deck in ship:
                if self.field_attack.get_cell(deck[0], deck[1]) != '1':
                    self.field_attack.set_cell(x, y, '1')
                    return

        self.__removing_dead_ship__(ship)
