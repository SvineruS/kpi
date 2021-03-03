import functools
import itertools

import numpy as np


SIZE = 8


class Game:

    def __init__(self, state):
        self.state = state
        self.self = self

    def get_board(self):
        """
            0: 1             0 1 0
            1: 2     <=>     0 0 2
            2: 1             0 3 0
            """
        board = np.zeros((SIZE, SIZE), dtype=np.int)
        for row, col in enumerate(self.state):
            board[row, col] = row + 1  # queen id
        return board

    def get_conflicts(self):
        def find_confilcts(cells):
            cells = list(filter(None, cells))
            return [frozenset((i, j)) for i, j in zip(cells, cells[1:])]

        board = self.get_board()
        confilcts = set()

        for i in range(-SIZE - 1, SIZE):
            if i >= 0:
                confilcts.update(find_confilcts(board[:, i]))
            confilcts.update(find_confilcts(board.diagonal(offset=i, axis1=0, axis2=1)))
            confilcts.update(find_confilcts(board.diagonal(offset=i, axis1=1, axis2=0)))

        return confilcts

    def f1(self):
        return len(self.get_conflicts())

    def is_no_confilcts(self):
        return not self.get_conflicts()

    def copy(self):
        return Game(self.state.copy())

    def __str__(self):
        return ''.join(map(str, self.state))


def _state_iter(start):
    return itertools.chain(range(start, SIZE), range(start))


def _base_alg(game, i=0, is_inf=False):
    if game.is_no_confilcts():
        return game
    if i == SIZE - 1:
        return None

    games = [game.copy() for game.state[i] in _state_iter(game.state[i])]

    if is_inf:
        games.sort(key=lambda g: g.f1())

    for g in games:
        res = alg_inf(g, i+1)
        if res is not None:
            return res


alg_no_inf = functools.partial(_base_alg, is_inf=False)
alg_inf = functools.partial(_base_alg, is_inf=True)
