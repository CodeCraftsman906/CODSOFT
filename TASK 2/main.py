import math

# ==============================
# Tic-Tac-Toe AI using Minimax
# Human : X
# AI    : O
# ==============================

board = [" " for _ in range(9)]

WINNING_COMBINATIONS = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]


# ==============================
# Display Functions
# ==============================

def show_position_guide():
    print("\nBoard Positions\n")

    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")


def display_board():

    print()

    for row in range(3):

        start = row * 3

        print(f" {board[start]} | {board[start+1]} | {board[start+2]} ")

        if row != 2:
            print("---+---+---")

    print()


# ==============================
# Player Input
# ==============================

def get_player_move():

    while True:

        try:

            position = int(input("Enter your move (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            position -= 1

            if board[position] != " ":
                print("That position is already occupied.")
                continue

            return position

        except ValueError:
            print("Invalid input! Please enter a number.")


# ==============================
# Game Logic
# ==============================

def make_move(position, player):
    board[position] = player


def check_winner(player):

    for combination in WINNING_COMBINATIONS:

        if all(board[pos] == player for pos in combination):
            return True

    return False


def check_draw():
    return " " not in board


def switch_player(player):

    if player == "X":
        return "O"

    return "X"


# ==============================
# AI Helper Functions
# ==============================

def get_available_moves():

    moves = []

    for i in range(9):

        if board[i] == " ":
            moves.append(i)

    return moves


def evaluate_board():

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    return 0


# ==============================
# Minimax Algorithm
# ==============================

def minimax(is_maximizing):

    score = evaluate_board()

    if score == 1:
        return 1

    if score == -1:
        return -1

    if check_draw():
        return 0

    # AI Turn
    if is_maximizing:

        best_score = -math.inf

        for move in get_available_moves():

            board[move] = "O"

            score = minimax(False)

            board[move] = " "

            best_score = max(best_score, score)

        return best_score

    # Human Turn
    else:

        best_score = math.inf

        for move in get_available_moves():

            board[move] = "X"

            score = minimax(True)

            board[move] = " "

            best_score = min(best_score, score)

        return best_score
    
# ==============================
# AI Move Selection
# ==============================

def get_best_move():
    """
    Determines the best move for the AI using the Minimax algorithm.
    """

    best_score = -math.inf
    best_move = None

    for move in get_available_moves():

        # Simulate AI move
        board[move] = "O"

        # Evaluate future game states
        score = minimax(False)

        # Undo move (Backtracking)
        board[move] = " "

        if score > best_score:
            best_score = score
            best_move = move

    return best_move


# ==============================
# Utility Functions
# ==============================

def reset_board():
    """
    Resets the game board for a new match.
    """

    global board
    board = [" " for _ in range(9)]


# ==============================
# Main Game
# ==============================

def play_game():

    current_player = "X"

    print("=" * 40)
    print("         TIC-TAC-TOE AI")
    print("=" * 40)

    show_position_guide()

    while True:

        print("\nCurrent Board")
        display_board()

        # ---------------- Human ----------------
        if current_player == "X":

            print("\nYour Turn (X)")
            move = get_player_move()

        # ---------------- AI ----------------
        else:

            print("\nAI is thinking...")

            move = get_best_move()

        make_move(move, current_player)

        # ---------------- Winner ----------------
        if check_winner(current_player):

            print("\nFinal Board")
            display_board()

            if current_player == "X":
                print("🎉 Congratulations! You Won!")
            else:
                print("🤖 AI Wins! Better luck next time.")

            break

        # ---------------- Draw ----------------
        if check_draw():

            print("\nFinal Board")
            display_board()

            print("🤝 It's a Draw!")

            break

        # Switch Turn
        current_player = switch_player(current_player)


# ==============================
# Program Entry
# ==============================

def main():

    while True:

        reset_board()

        play_game()

        choice = input("\nDo you want to play again? (Y/N): ").strip().lower()

        if choice != "y":
            print("\nThank you for playing Tic-Tac-Toe AI!")
            break


if __name__ == "__main__":
    main()