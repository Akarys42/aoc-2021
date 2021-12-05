from typing import Optional
import itertools


with open('day_4/input.txt') as file:
    INPUT = [int(num) for num in file.readline().split(",")]

    # Consume the empty line
    file.readline()

    BOARDS = [[[int(n) for n in line.split()] for line in board.split("\n")] for board in file.read().split("\n\n")]


Board = list[list[Optional[int]]]

def mark_board(board: Board, chosen: int) -> None:
    for line in board:
        for i, num in enumerate(line):
            if num == chosen:
                line[i] = None


def check_board(board: Board) -> bool:
    for i in range(len(board)):
        # Check the i row
        if all(num is None for num in board[i]):
            return True
        
        # Check the i column
        if all(line[i] is None for line in board):
            return True
    
    return False

for number in INPUT:
    for board in BOARDS:
        mark_board(board, number)

        if check_board(board):
            print(sum(num for num in itertools.chain(*board) if num is not None) * number)
            exit()