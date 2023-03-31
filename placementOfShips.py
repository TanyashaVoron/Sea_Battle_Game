from playingFiel import playingField


class placementOfShips:
    """
    cur_state:
    0 - wait next ship
    1 - wait choose direction

    ships: 1, 2, 3, 4 - decks
    """

    def __init__(self):
        self.field = playingField()
        self.cur_state = 0
        self.cur_ship_index = 0
        self.array_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        self.last_cell = [0, 0]

    def get_cell(self, i, j):
        return self.field.get_cell(i, j)

    def set_cell(self, i, j, val):
        self.field.set_cell(i, j, val)

    def put_ship(self, i, j):
        # выставляется первая палуба нового корабля
        if self.cur_state == 0:
            if self.get_cell(i, j) == "0":
                self.set_cell(i, j, "3")
                self.cur_state = 1
                self.last_cell = [i, j]

                # показ возможных направлений для текущего корабля
                self.show_free_directions(i, j, self.array_of_ships[self.cur_ship_index])

        # выставляются остальные палубы корабля
        elif self.cur_state == 1:
            self.remove_question_marks()
            k = self.array_of_ships[self.cur_ship_index]
            if k == 1:
                self.cur_state = 0
            else:
                direction = self.choose_direction(i, j)
                if direction == "up":
                    for m in range(1, k):
                        self.set_cell(self.last_cell[0] - m, j, "3")
                    self.cur_state = 0
                    self.cur_ship_index += 1
                elif direction == "right":
                    for m in range(1, k):
                        self.set_cell(i, self.last_cell[1] + m, "3")
                    self.cur_state = 0
                    self.cur_ship_index += 1
                elif direction == "down":
                    for m in range(1, k):
                        self.set_cell(self.last_cell[0] + m, j, "3")
                    self.cur_state = 0
                    self.cur_ship_index += 1
                elif direction == "left":
                    for m in range(1, k):
                        self.set_cell(i, self.last_cell[1] - m, "3")
                    self.cur_state = 0
                    self.cur_ship_index += 1

    def choose_direction(self, i, j):
        difference = [self.last_cell[0] - i, self.last_cell[1] - j]
        if difference[0] > 0 and difference[1] == 0:
            return "up"
        if difference[0] == 0 and difference[1] < 0:
            return "right"
        if difference[0] < 0 and difference[1] == 0:
            return "down"
        if difference[0] == 0 and difference[1] > 0:
            return "left"

    def show_free_directions(self, i, j, k):
        if self.check_free_directions(i, j, "up"):
            for m in range(1, k):
                self.set_cell(i - m, j, "?")
        if self.check_free_directions(i, j, "right"):
            for m in range(1, k):
                self.set_cell(i, j + m, "?")
        if self.check_free_directions(i, j, "down"):
            for m in range(1, k):
                self.set_cell(i + m, j, "?")
        if self.check_free_directions(i, j, "left"):
            for m in range(1, k):
                self.set_cell(i, j - m, "?")

    # проверка направлений на то, что там нет других кораблей, и там не конец поля
    def check_free_directions(self, i, j, dir):
        k = self.array_of_ships[self.cur_ship_index]
        if dir == "up":
            # проверка на то, что там нет кораблей
            try:
                for m in range(1, k):
                    if self.get_cell(i - m, j) != "0":
                        return False
            except IndexError:
                return False
            # проверка на то, что корабль будет стоять у края поля
            try:
                if self.get_cell(i - k, j) == "3":
                    return False
            except IndexError:
                return True

            return True

        if dir == "right":
            try:
                for m in range(1, k):
                    if self.get_cell(i, j + m) != "0":
                        return False
            except IndexError:
                return False

            try:
                if self.get_cell(i, j + k) == "3":
                    return False
            except IndexError:
                return True

            return True

        if dir == "down":
            try:
                for m in range(1, k):
                    if self.get_cell(i + m, j) != "0":
                        return False
            except IndexError:
                return False

            try:
                if self.get_cell(i + k, j) == "3":
                    return False
            except IndexError:
                return True

            return True

        if dir == "left":
            try:
                for m in range(1, k):
                    if self.get_cell(i, j - m) != "0":
                        return False
            except IndexError:
                return False

            try:
                if self.get_cell(i, j - k) == "3":
                    return False
            except IndexError:
                return True

            return True

    def remove_question_marks(self):
        for i in range(1, self.field.n):
            for j in range(1, self.field.n):
                if self.get_cell(i, j) == "?":
                    self.set_cell(i, j, "0")


if __name__ == '__main__':
    A = placementOfShips()
    A.put_ship(4, 1)
    print(A.field)
    A.put_ship(3, 1)

    A.put_ship(9, 8)
    print(A.field)
    A.put_ship(9, 7)

    A.put_ship(2, 4)
    print(A.field)
    A.put_ship(2, 5)

    A.put_ship(2, 10)
    print(A.field)
    A.put_ship(2, 9)

    A.put_ship(6, 7)
    print(A.field)
    A.put_ship(5, 7)

    A.put_ship(5, 4)
    print(A.field)
    A.put_ship(6, 4)

    A.put_ship(8, 2)
    print(A.field)
    A.put_ship(7, 2)

    A.put_ship(8, 4)
    print(A.field)
    A.put_ship(8, 5)

    A.put_ship(7, 9)
    print(A.field)
    A.put_ship(3, 9)

    A.put_ship(4, 9)
    print(A.field)
    A.put_ship(4, 6)

    print(A.field)
