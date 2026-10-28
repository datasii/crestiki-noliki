from board import create_board, print_board
from check_win import check_win

board = create_board()
board[0][0] = 'X'
board[1][1] = 'X'
board[2][2] = 'X'
print_board(board)
print("Победа X:", check_win(board, 'X'))
