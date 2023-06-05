from Field.PlacementOfStraightShips import placementOfStraightShips


class placementOfAngularShips(placementOfStraightShips):
    def __init__(self, field, field_size):
        super().__init__(field, field_size)
        self.number_of_exposed_cells = 0

    def put_ship(self, i, j):
        k = self.array_of_ships[self.cur_ship_index]
        # проверка на корректность ввода
        if not self.checking_the_correct_direction(i, j):
            return

        self.set_cell(i, j, "3")
        self.number_of_exposed_cells += 1

        if self.number_of_exposed_cells == k:
            self.number_of_exposed_cells = 0
            self.remove_question_marks()
            self.fence_of_cells(i, j)
            self.remove_plus_marks()
            self.cur_ship_index += 1
        else:
            self.show_free_directions(i, j)

        if self.cur_ship_index == len(self.array_of_ships):
            self.remove_exclamation_marks()

    def checking_the_correct_direction(self, i, j):
        """
        проверка на то, что игрок выбрал правильное направление для выставления корабля
        """
        if self.number_of_exposed_cells == 0:
            return self.get_cell(i, j) == "0"
        return self.get_cell(i, j) == "?"

    def show_free_directions(self, i, j, **kwargs):
        """
        показ возможных направлений для постановки текущего корабля
        """
        if self.check_free_direction(i, j, "up"):
            self.set_cell(i - 1, j, "?")
        if self.check_free_direction(i, j, "right"):
            self.set_cell(i, j + 1, "?")
        if self.check_free_direction(i, j, "down"):
            self.set_cell(i + 1, j, "?")
        if self.check_free_direction(i, j, "left"):
            self.set_cell(i, j - 1, "?")

    def check_free_direction(self, i, j, dir):
        """
        проверка направлений на то, что там нет других кораблей, и там не конец поля
        """
        initial_value_i = i
        initial_value_j = j

        # проверка на то, что нет других кораблей
        try:
            i = initial_value_i
            j = initial_value_j
            if dir == "up":
                i = i - 1
            if dir == "right":
                j = j + 1
            if dir == "down":
                i = i + 1
            if dir == "left":
                j = j - 1

            if self.get_cell(i, j) != "0":
                return False
        except IndexError:
            return False

        i = initial_value_i
        j = initial_value_j
        try:
            if dir == "up":
                i = i - 1
            if dir == "right":
                j = j + 1
            if dir == "down":
                i = i + 1
            if dir == "left":
                j = j - 1

            if self.get_cell(i, j) == "3":
                return False
        except IndexError:
            return True

        return True

    def fence_of_cells(self, i, j):
        """
        ограждение корабля во избежании того, чтобы последующие стояли рядом.
        Поиск в ширину по кораблю
        """
        array_of_surrounding_cells = [[i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1],
                                      [i + 1, j], [i + 1, j - 1], [i, j - 1], [i - 1, j - 1]]
        self.set_cell(i, j, "+")

        cur_idx = 0
        for l in range(8):
            try:
                temp_i = array_of_surrounding_cells[cur_idx][0]
                temp_j = array_of_surrounding_cells[cur_idx][1]

                if self.get_cell(temp_i, temp_j) == "0":
                    self.set_cell(temp_i, temp_j, "!")
                elif self.get_cell(temp_i, temp_j) == "3":
                    self.fence_of_cells(temp_i, temp_j)
                cur_idx += 1
            except IndexError:
                cur_idx += 1

    def remove_plus_marks(self):
        """
        очищение поля от временных плюсиков
        """
        for i in range(1, self.field.n):
            for j in range(1, self.field.n):
                if self.get_cell(i, j) == "+":
                    self.set_cell(i, j, "3")
