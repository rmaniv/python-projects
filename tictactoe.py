import itertools

# Win checker =========================================================

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally (-)!")
            return True

    # Diagonal
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])

    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (/)!")
        return True


    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} is the winner diagonally (\\)!")
        return True

    # Verical
    for col in range(len(game)):
        check = []

    for row in game:
        check.append(row[col])

    if all_same(check):
        print(f"Player {check[0]} is the winner vertically (|)!")
        return True
    
    return False

# Game board =========================================================

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    
    try:
        if game_map[row][column] != 0:
            print("This position is occupied, choose another!")
            return False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map

    except IndexError as e:
        print("Error: did you input row/column as 0 1 or 2?", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

# Play =========================================================

play = True
players = [1, 2]

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    player_choice = itertools.cycle([1, 2])
    game_board(game, just_display=True) # initial display

    while not game_won:
        current_player = next(player_choice)
        played = False
        while not played:
            print(f"Current Player: {current_player}")
            row_choice = int(input("Enter the row (0, 1, 2): "))
            column_choice = int(input("Enter the column (0, 1, 2): "))
            played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Would you like to play again? (y/n) ")
            if again.lower() == 'y':
                print("Restarting...")
            elif again.lower() == 'n':
                print("Bye...")
                play = False
            else:
                print("Not a valid input, bye anyways...")
                play = False
