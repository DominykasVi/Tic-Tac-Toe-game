from random import randint


class BoardClass:

    def __init__(self):
        self.board = {}
        self.create_board()
        self.positions = []

    def create_board(self):
        for i in range(0, 9):
            self.board[i] = "-"

    def print_board(self):
        count = 0
        print("#####################")
        for i in range(0, 9):
            count += 1
            if count % 3 == 0:
                print(self.board[i], end='')
                print()
                continue
            print(self.board[i], end='')
            print(" | ", end='')

    def enter_guess(self, position, symbol):
            self.board[position] = symbol
            self.positions.append(position)

    def check_guess(self, guess):
        for i in self.positions:
            if i == guess:
                return False
        return True

    def check_if_winner(self, symbol):
        if self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol:
            return True
        elif self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol:
            return True
        elif self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol:
            return True
        elif self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol:
            return True
        elif self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol:
            return True
        elif self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol:
            return True
        elif self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol:
            return True
        elif self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol:
            return True
        else:
            return False


def number_validation(symbol):
    num = -1
    while num <= 0 or num > 9:
        while True:
            num = input(symbol + "'s turn(enter value from 1 to 9): ")
            try:
                num = int(num)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")
    return num


win = False
board = BoardClass()
choice = input("Do you want to play against a bot?[Y/N]: ")#Validate input!!!
if choice.lower() == "y":
    bot = True
    player_symbol = input("Do you want to play as X or O?: ")#Validate input!!!
    # print(player_symbol.lower() == "x")
    if player_symbol.lower() == "x":
        bot_symbol = "O"
    else:
        bot_symbol = "X"
else:
    bot = False
    bot_symbol = "Y"

for i in range(1, 10):
    board.print_board()
    if i % 2 == 0:
        symbol = "O"
        if symbol == bot_symbol:
            random = randint(1, 9)
            while not board.check_guess(random-1):
                random = randint(1, 9)
            board.enter_guess(random-1, symbol)
            print("Bots guess ", end='')
            print(random)
            if board.check_if_winner(symbol):
                print("Bot won, better luck next time.")
                win = True
                board.print_board()
                break
            continue
    else:
        symbol = "X"
        if symbol == bot_symbol:
            random = randint(1, 9)
            while not board.check_guess(random-1):
                random = randint(1, 9)
            board.enter_guess(random-1, symbol)
            print("Bots guess ", end='')
            print(random)
            if board.check_if_winner(symbol):
                print("Bot won, better luck next time.")
                win = True
                board.print_board()
                break
            continue
    while True:
        num = number_validation(symbol)
        if board.check_guess(num-1):
            board.enter_guess(num-1, symbol)
            break
        else:
            print("Positions already taken")
    if board.check_if_winner(symbol):
        print("Congratulations " + symbol + "!!! You won the game")
        board.print_board()
        win = True
        break

if not win:
    print("It's a tie!")
