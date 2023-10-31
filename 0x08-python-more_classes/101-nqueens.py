#!/usr/bin/python3
"""solving the N queen challenge (it is about chess)"""
import sys


class NQueensSolver():
    """Defining the NQueensSolver class"""

    def __init__(self, N):
        self.N = N
        self.chessboard = [[" "] * N for i in range(N)]

        self.used_columns = set()          # Tracks used columns
        self.used_right_diagonals = set()  # Tracks used right diagonals
        self.used_left_diagonals = set()   # Tracks used left diagonals

        self.solutions = []  # A list to store found solutions

    def solve(self):
        self.find_Queen()
        for solution in self.solutions:
            print(solution)

    def find_Queen(self, row=0):
        if row == self.N:
            result = []
            for row in self.chessboard:
                [result.append(pos) for pos in row if pos != " "]
            self.solutions.append(result)
            return

        for col in range(self.N):
            if (col in self.used_columns or
                (row + col) in self.used_right_diagonals or
                    (row - col) in self.used_left_diagonals):
                continue

            self.used_columns.add(col)
            self.used_right_diagonals.add(row + col)
            self.used_left_diagonals.add(row - col)
            self.chessboard[row][col] = [row, col]

            self.find_Queen(row + 1)

            self.used_columns.remove(col)
            self.used_right_diagonals.remove(row + col)
            self.used_left_diagonals.remove(row - col)
            self.chessboard[row][col] = " "


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    queens_solver = NQueensSolver(N)
    queens_solver.solve()
