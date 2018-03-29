def tic_tac_toe():
	board = [None] + list(range(1,10))
	WIN_COMBINATIONS = [
	(1, 2, 3),
	(4, 5, 6),
	(7, 8, 9),
	(1, 5, 9),
	(3, 5, 7),
	(1, 4, 7),
	(2, 5, 9),
	(3, 6, 9),
	]
	
	def draw():
		print("-------------")
		print("|", board[7], "|", board[8], "|", board[9], "|")
		print("-------------")
		print("|", board[4], "|", board[5], "|", board[6], "|")
		print("-------------")
		print("|", board[1], "|", board[2], "|", board[3], "|")
		print("-------------")
	
	def choose_space():
		while True:
			try:
				choice = int(input("Choose a number to place your token: "))
				if choice in board:
					return choice
				else:
					print("\nInvalid move, please try again.")
			except ValueError:
				print("\nThat's not a valid position, please try again.")
	
	def is_game_over():
		for a, b, c in WIN_COMBINATIONS:
			if board[a] == board[b] == board[c]:
				print("Player {0} wins!\n".format(board[a]))
				print("Woo!\n")
				return True
		if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
			print("The game is tied\n")
			return True
	
	for player in 'XO' * 9:
		draw()
		if is_game_over():
			break
		print("Player {0} pick your move".format(player))
		board[choose_space()] = player
		print()
	
while True:
	tic_tac_toe()
	if input("Play again (y/n)\n") != "y":
		break

