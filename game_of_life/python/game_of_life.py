#!/usr/bin/python3 env
from collections import namedtuple

# Used throughout
Point = namedtuple('Point', ['x', 'y'])
Point.__add__ = lambda self, other: Point(self.x + other.x, self.y + other.y)


def neighbours(p: Point):
    adjacents = [
        # Up and right
        Point(1, 0), Point(0, 1),
        # Down and left
        Point(-1, 0), Point(0, -1),
        # Diagonally (up+down) and left
        Point(1, -1), Point(-1, -1),
        # Diagonally (up+down) and right
        Point(-1, 1), Point(1, 1),
    ]
    for neighbour in adjacents:
        yield p + neighbour


def advance(board: set, turns: int, required_neighbours: int=3):
    from itertools import chain

    new_board = board.copy()
    for _ in range(abs(turns)):
        next_state = set()
        next_iteration = new_board | set(chain(*map(neighbours, new_board)))
        for point in next_iteration:
            count = sum((neigh in new_board) for neigh in neighbours(point))
            if (count == required_neighbours or
               # Also handle corners:
               (count == (required_neighbours - 1) and point in new_board)):
                next_state.add(point)
        new_board = next_state
    return new_board


if __name__ == '__main__':
    # Example from: https://youtu.be/o9pEzgHorH0?t=1167
    start_glider = set([
        Point(0, 0), Point(1, 0), Point(2, 0),
        Point(0, 1), Point(1, 2)
    ])

    received_glider = advance(board=start_glider, turns=2002)
    expected_glider = set([
        Point(-500, -501), Point(-500, -500), 
        Point(-500, -499), Point(-499, -501), 
        Point(-498, -500),
    ])

    assert received_glider == expected_glider
    print("Simple 2002x iterations glider-test passed!")
