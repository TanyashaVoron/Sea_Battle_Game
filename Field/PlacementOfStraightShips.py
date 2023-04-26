class placementOfStraightShips:
    """
    cur_state:
    0 - wait next ship
    1 - wait choose direction

    ships: 1, 2, 3, 4 - decks
    """

    def __init__(self, field, field_size):
        self.field_size = field_size  # размер поля
        self.field = field
        self.cur_state = 0  # 0 - выставление первой палубы, 1 - выбор направления
        self.cur_ship_index = 0  # размер текущего выставляемого корабля
        self.array_of_ships = None  # набор всех кораблей для данного размера поля
        self.count_array_of_ships()
        self.last_cell = [0, 0]  # последняя выбранная ячейка

    # Этот метод из интерфейса
    def count_array_of_ships(self):
        if self.field_size == 10:
            self.array_of_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
        elif self.field_size == 15:
            self.array_of_ships = [5, 4, 4, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1]
        elif self.field_size == 20:
            self.array_of_ships = [6, 5, 5, 4, 4, 4, 3, 3, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]

    def get_cell(self, i, j):
        return self.field.get_cell(i, j)

    def set_cell(self, i, j, val):
        self.field.set_cell(i, j, val)

    def end_of_placement(self):
        if self.cur_ship_index == len(self.array_of_ships):
            return True
        return False

    def put_ship(self, i, j):

        # выставляется первая палуба нового корабля
        if self.cur_state == 0:
            if self.get_cell(i, j) == "0":
                self.set_cell(i, j, "3")
                self.cur_state = 1
                self.last_cell = [i, j]

                # если сейчас ставится однопалубник, то напрвление выбирать не надо
                if self.array_of_ships[self.cur_ship_index] == 1:
                    self.cur_state = 0
                    self.set_cell(i, j, "3")
                    self.fence_off_cell(self.last_cell[0], self.last_cell[1])
                    self.cur_ship_index += 1

                    if self.cur_ship_index == 10:
                        self.remove_exclamation_marks()
                else:
                    # показ возможных направлений для текущего корабля
                    self.show_free_directions(i, j, self.array_of_ships[self.cur_ship_index])
            else:
                return

        # выставляются остальные палубы корабля в зависимости от выбранного направления
        elif self.cur_state == 1:
            k = self.array_of_ships[self.cur_ship_index]
            # TODO: вставить проверку на то, что игрок выбрал из правильных направлений
            direction = self.choose_direction(i, j)

            # TODO: надо придумать, как уведомлять игорка о том, что он выбрал неправильное направление
            if not self.checking_the_correct_direction(i, j):
                return
            self.remove_question_marks()

            if direction == "up":
                for m in range(1, k):
                    self.set_cell(self.last_cell[0] - m, j, "3")
                self.cur_state = 0
                self.fence_off_ship("up")
                self.cur_ship_index += 1
            elif direction == "right":
                for m in range(1, k):
                    self.set_cell(i, self.last_cell[1] + m, "3")
                self.cur_state = 0
                self.fence_off_ship("right")
                self.cur_ship_index += 1
            elif direction == "down":
                for m in range(1, k):
                    self.set_cell(self.last_cell[0] + m, j, "3")
                self.cur_state = 0
                self.fence_off_ship("down")
                self.cur_ship_index += 1
            elif direction == "left":
                for m in range(1, k):
                    self.set_cell(i, self.last_cell[1] - m, "3")
                self.cur_state = 0
                self.fence_off_ship("left")
                self.cur_ship_index += 1

    # проверка на то, что игрок выбрал правильное направление для выставления корабля
    def checking_the_correct_direction(self, i, j):
        return self.get_cell(i, j) == "?"

    # понимание, какое напрвление выбрал игрок
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

    # показ возможных направлений для постановки текущего корабля
    def show_free_directions(self, i, j, k):
        if self.check_free_direction(i, j, "up"):
            for m in range(1, k):
                self.set_cell(i - m, j, "?")
        if self.check_free_direction(i, j, "right"):
            for m in range(1, k):
                self.set_cell(i, j + m, "?")
        if self.check_free_direction(i, j, "down"):
            for m in range(1, k):
                self.set_cell(i + m, j, "?")
        if self.check_free_direction(i, j, "left"):
            for m in range(1, k):
                self.set_cell(i, j - m, "?")

    # проверка направлений на то, что там нет других кораблей, и там не конец поля
    def check_free_direction(self, i, j, dir):
        k = self.array_of_ships[self.cur_ship_index]
        initial_value_i = i
        initial_value_j = j

        # проверка на то, что нет других кораблей
        try:
            for m in range(1, k):
                i = initial_value_i
                j = initial_value_j
                if dir == "up":
                    i = i - m
                if dir == "right":
                    j = j + m
                if dir == "down":
                    i = i + m
                if dir == "left":
                    j = j - m

                if self.get_cell(i, j) != "0":
                    return False
        except IndexError:
            return False

        # проверка на то, что корабль будет стоять у края поля
        i = initial_value_i
        j = initial_value_j
        try:
            if dir == "up":
                i = i - k
            if dir == "right":
                j = j + k
            if dir == "down":
                i = i + k
            if dir == "left":
                j = j - k

            if self.get_cell(i, j) == "3":
                return False
        except IndexError:
            return True

        return True

    # ограждение корабля во избежании того, чтобы последующие стояли рядом
    def fence_off_ship(self, dir):
        k = self.array_of_ships[self.cur_ship_index]
        i = self.last_cell[0]
        j = self.last_cell[1]

        initial_value_i = i
        initial_value_j = j

        for m in range(0, k):
            i = initial_value_i
            j = initial_value_j
            if dir == "up":
                i = i - m
            if dir == "right":
                j = j + m
            if dir == "down":
                i = i + m
            if dir == "left":
                j = j - m

            self.fence_off_cell(i, j)

    # ограждение одной клетки
    def fence_off_cell(self, i, j):
        array_of_surrounding_cells = [[i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1],
                                      [i + 1, j], [i + 1, j - 1], [i, j - 1], [i - 1, j - 1]]

        cur_idx = 0
        for l in range(8):
            try:
                temp_i = array_of_surrounding_cells[cur_idx][0]
                temp_j = array_of_surrounding_cells[cur_idx][1]

                if self.get_cell(temp_i, temp_j) == "0":
                    self.set_cell(temp_i, temp_j, "!")
                cur_idx += 1
            except IndexError:
                cur_idx += 1

    # очищение поля от показа направлений для постановки предыдущего корабля
    def remove_question_marks(self):
        for i in range(1, self.field.n):
            for j in range(1, self.field.n):
                if self.get_cell(i, j) == "?":
                    self.set_cell(i, j, "0")

    # очищение поля от ограждающих отметок
    def remove_exclamation_marks(self):
        for i in range(1, self.field.n):
            for j in range(1, self.field.n):
                if self.get_cell(i, j) == "!":
                    self.set_cell(i, j, "0")


if __name__ == '__main__':
    pass
