import json
from permutor import show_board

board_post = 9

player1 = []
player2 = []


post = int(input("Post: "))
piece = input("Piece: ")


def set_piece(post, piece):
    with open('game_board.json') as f:
        data = json.load(f)

        counter = 0 

        for i in data["board"]:
            if data["board"][counter]["post"] == post:
                if data["board"][counter]["filled"] == False:
                    data["board"][counter]["piece"] = piece
                    data["board"][counter]["filled"] = True
                else:
                    print("There is a piece already on this post\n")
                    break
            
            with open('game_board.json', 'w') as f:
                json.dump(data, f, indent=2)

            counter += 1

            

def move_piece(post, piece):

    post = post - 1 # this is to make looping effective

    with open('game_board.json') as f:
        data = json.load(f)

    counter = 0 

    for i in data["board"]:
        previous_post = data["board"][counter]
        next_post = data["board"][post]
        
        if next_post["filled"] == False:    
            if previous_post["piece"] == piece:
                if previous_post["filled"] == True:

                    previous_post["piece"] = None
                    previous_post["filled"] = False

                    next_post["piece"] = piece
                    next_post["filled"] = True

                    with open('game_board.json', 'w') as f:
                        json.dump(data, f, indent=2)

        counter += 1


def capture_board():
    with open('game_board.json') as f:
        data = json.load(f)

        counter = 0

        board = []

        player1_win = []
        player2_win = []

        results = show_board()

        for i in data["board"]:
            if data["board"][counter]["filled"] == True:
                current_board = data["board"][counter]


                if current_board["piece"] in player1:
                    player1_win.append(current_board["post"])


                elif current_board["piece"] in player2:
                    player2_win.append(current_board["post"])
                        
                        
                board.append( (current_board["post"], current_board["piece"]) )

            counter += 1


        print(board)    

        player1_win = str(player1_win)[1:-1]
        player1_win = f"({player1_win})"

        player2_win = str(player2_win)[1:-1]
        player2_win = f"({player2_win})"


        if player1_win in results:
            print(f"Player 1 has won: {player1_win}")
        elif player2_win in results:
            print(f"Player 2 has won: {player2_win}")



# set = set_piece(post=post, piece=piece)

move = move_piece(post=post, piece=piece)

capture_board()