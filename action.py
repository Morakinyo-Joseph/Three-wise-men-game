import json
from permutor import show_board


def set_piece(post, piece):
    player_1 = None
    player_2 = None

    with open('game_board.json') as f:
        data = json.load(f)

        counter = 0

        for i in data["board"]:

            if data["board"][counter]["post"] == post:
                if data["board"][counter]["filled"] == False:
                    data["board"][counter]["piece"] = piece
                    data["board"][counter]["filled"] = True

                    # to get the number of pieces for each player
                    if counter == 0:
                        player_1 = (data["board"][counter]["piece"])
                    elif counter % 2 == 0:
                        player_1 = (data["board"][counter]["piece"])
                    else:
                        player_2 = (data["board"][counter]["piece"])


                else:
                    print("There is a piece already on this post\n")
                    break

            with open('game_board.json', 'w') as f:
                json.dump(data, f, indent=2)

            counter += 1
        
        # this will be returned for further processing
        # players = {
        #     "player1": player_1,
        #     "player2": player_2
        # }

    if player_1:
        return player_1
    elif player_2:
        return player_2


            

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

                    p_post = previous_post["post"]

                    previous_post["piece"] = None
                    previous_post["filled"] = False

                    next_post["piece"] = piece
                    next_post["filled"] = True

                    with open('game_board.json', 'w') as f:
                        json.dump(data, f, indent=2)

        counter += 1

    return p_post


def capture_board(player1, player2):
    
    player1_win = []
    player2_win = []
    
    with open('game_board.json') as f:
        data = json.load(f)

        counter = 0

        board = []

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

        player1_win = str(player1_win)[1:-1]
        player1_win = f"({player1_win})"

        player2_win = str(player2_win)[1:-1]
        player2_win = f"({player2_win})"



    if player1_win in results:
        message = f"\nPlayer 1 has won: {player1_win}\n"
        return message
    elif player2_win in results:
        message = f"\nPlayer 2 has won: {player2_win}\n"
        return message
    else:
        return board




def reset_board():
    with open('game_board.json') as f:
        data = json.load(f)

        counter = 0

        for i in data["board"]:
            if data["board"][counter]["filled"] == True:
                data["board"][counter]["piece"] = None
                data["board"][counter]["filled"] = False

                with open('game_board.json', 'w') as f:
                    json.dump(data, f, indent=2)

            counter += 1