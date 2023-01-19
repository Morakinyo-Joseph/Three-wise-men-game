from action import set_piece, move_piece, capture_board, reset_board

def three_wise_men():
        
    player1 = []
    player2 = []

    try:
            
        while True:
                
            print(
                '''
        THREE WISE MEN
        --------------

        a: Start game     


        b: quit

                '''
            )

            report = input("\ninput:  ")

            if report == "a" or report == "A":
                
                # game's homepage
                def game():

                    print(
                        '''

        a: Set Piece        b: Move Piece

        c: view Board       d: How to Play

        e: Reset Board

        End game: ctrl + c
                        '''
                    )

                    report2 = input("\ninput: ")

                    if report2 == "a" or report2 == "A":    
                        
                        checking = 0

                        if len(player1) == 3:
                            print("\n>>> Pieces on board are already complete")
                            game()

                        while checking < 6:

                            post = int(input("\nPoint: "))
                            piece = input("Piece: ")

                            piece_placing = set_piece(post=post, piece=piece)

                            counter = 0
                            flag = None  # flag is used for confirmation 

                            if piece_placing:    
                                for i in piece_placing:
                                    if i[counter] == "w":
                                        flag = True
                                    elif i[counter] == "b":
                                        flag = False

                            if flag:
                                player1.append(piece_placing)
                            elif flag == False:
                                player2.append(piece_placing)

                            checking += 1

                            # display current board stats
                            display = capture_board(player1, player2)

                            # checks whether a player won in setting
                            if "Player" in display:
                                print(display)

                                reset_board()
                                print("-------------------")

                                player1.clear()
                                player2.clear()

                                three_wise_men()

                            print(display)
                            
                            
                        else:
                            print("\n>>> All pieces are on board already")
                            game()
                        
                        # display current board stats
                        display = capture_board(player1, player2)
                        print(display)

                    # move a piece on the board
                    elif report2 == "b" or report2 == "B":
                        if len(player1) != 3:
                            print("\n>>> Pieces hasn't being set yet")
                            game()

                        post = int(input("\nMove to Point: "))
                        piece = input("\nWhat Piece: ")
                        if post % 1 != post:
                            print("\n>>> Such point does not exists!")
                            game()
                        elif piece not in player1 or piece not in player2:
                            print("\n>>> Such Piece does not exists!")
                            game()

                        piece_moving = move_piece(post=post, piece=piece)
                        print(f"\n>>> {piece} has being moved from point({piece_moving}) to point({post}) successfully")
                        game()

                        # display current board stats
                        display = capture_board(player1, player2)

                        if "Player" in display:
                            print(display)

                            reset_board()
                            print("-------------------")
                            
                            player1.clear()
                            player2.clear()

                            three_wise_men()

                        print(display)
                        
                    # view the board
                    elif report2 == "c" or report2 == "C":
                        
                        if len(player1) != 3:
                            print("\n>>> Nothing to view on board")
                            game()

                        display = capture_board(player1, player2)
                        print("\n\n")
                        print(display)
                        game()

                    # how to play
                    elif report2 == "d" or report2 == "D":
                        print(
                            '''
        -THREE WISE MEN-
        
            Three wise men is an advanced level of the renowed Tic-tak-toe game.

        SETTING YOUR PIECES
        ------------------- 
        1: This is a two player game whereby taking turns is advised.

        2: The first person to start is player one followed by player two.

        3: Player One has three pieces > w1, w2 and w3.
            Player Two has three pieces > b1, b2 and b3.

            Note: any other input apart from these won't work.

        4: There is a total of Nine (9) points on the board.

        5: Each player, starting from the first player has to select a point on the board and select a piece to put there.

        
        MOVING YOUR PIECES
        ------------------
        1: The next player to move a piece will do so after the last player has set their last piece.

        2: To move a piece, select a point that is not occupied with a piece and input one of your's there.

            Note: Before selecting the option "Move Piece", check 'View Board' to view available points.

        3: Once this is done, the next player can do thesame with their own pieces.

        
        WINNING A MATCH
        ---------------
            1: Winning a match will be as a result of you setting and moving your pieces wisely

            2: For a player to win, all three pieces must be in alignment on the POINTS of board.
            
            This ranges from:
                    (1, 2, 3)
                    (4, 5, 6)
                    (7, 8, 9)
                    (1, 4, 7)
                    (2, 5, 8)
                    (3, 6, 9)
                    (1, 5, 9)
                    (3, 5, 8)

                            '''
                        )
                        game()

                    # reset board
                    elif report2 == "e" or report2 == "E":
                        reset_board()
                        player1.clear()
                        player2.clear()
                        print("\n>>> Board has being reset!")
                        game()


                    else:
                        print("\n>>> Sorry Invalid Input!")
                        game()           
                
            elif report == "":
                print("\n>>> Did not receieve any input\n")
                three_wise_men()

            elif report == "b" or report == "B":
                break
            else:
                print(f"\n>>> '{report}' is not an allowed response ")
                three_wise_men()
            
                

            game()

    except KeyboardInterrupt:
        print("\n\n>>> Thanks for playing...\n")
        reset_board()



three_wise_men()