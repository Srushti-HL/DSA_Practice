class Solution:
    def tictactoe(self, moves):
        board = [['' for _ in range(3)] for _ in range(3)]

        for i, (row, col) in enumerate(moves):
            if i % 2 == 0:
                board[row][col] = 'A'
            else:
                board[row][col] = 'B'

        # Check rows
        for row in board:
            if row[0] != '' and row[0] == row[1] == row[2]:
                return row[0]

        # Check columns
        for col in range(3):
            if board[0][col] != '' and board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]

        # Check diagonals
        if board[0][0] != '' and board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]

        if board[0][2] != '' and board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

        # No winner
        if len(moves) == 9:
            return "Draw"

        return "Pending"