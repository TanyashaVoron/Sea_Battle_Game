import enum


# возможные сотояния клетки
class state_cell(enum.Enum):
    free = 0        # свободная
    killed = 1      # подстреленная
    past = 2        # удар был, но мимо
    ship = 3        # стоит целая часть корабля
