import random


# Print board
def print_board(board):
    print("+---+---+---+")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i * 3 + j], end=" | ")
        print("\n+---+---+---+")


# Check who is the winner
def check_winner(board):
    winning_combos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":
            return board[combo[0]]
    return None


# Get human move
def get_human_move(board):
    while True:
        move = input("Enter a move (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move) - 1] != " ":
            print("Invalid move, try again.")
            continue
        return int(move) - 1


# Get computer move
def get_computer_move(board):
    available_moves = [i for i in range(9) if board[i] == " "]

    # Check if any move can win the game
    for move in available_moves:
        test_board = list(board)
        test_board[move] = "O"
        if check_winner(test_board) == "O":
            return move

    # Check if any move can prevent the human from winning the game
    for move in available_moves:
        test_board = list(board)
        test_board[move] = "X"
        if check_winner(test_board) == "X":
            return move

    # Choose a random available move
    return random.choice(available_moves)


def main():
    board = [" " for i in range(9)]
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        if " " not in board:
            print("Tie!")
            break
        if len([i for i in board if i != " "]) % 2 == 0:
            move = get_computer_move(board)
            board[move] = "O"
            print(f"Computer played move {move + 1}.")
        else:
            move = get_human_move(board)
            board[move] = "X"
            print(f"Human played move {move + 1}.")


if __name__ == "__main__":
    main()
