from playingFiel import playingField


class placementOfShips:
    def __init__(self):
        self.field = playingField()

    def get_cell(self, i, j):
        return self.field.get_cell(i, j)

    def set_cell(self, i, j, val):
        self.field.set_cell(i, j, val)
