def check_win(board, player):
	for i in range(3):
		if all(board[i][j] == player for j in range(3)): return True
		if all(board[j][i] == player for j in range(3)): return True
	if board[0][0] == board[1][1] == board[2][2] == player: return True
	if board[0][2] == board[1][1] == board[2][0] == player: return True
	return False


