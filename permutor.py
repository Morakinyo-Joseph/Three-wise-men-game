import json
from itertools import permutations


def show_board():
    with open('game_board.json') as f:
        data = json.load(f)

        counter = 0

        # getting all posts in a list
        lineup = []
        for i in data["board"]:
            post = data["board"][counter]["post"]
        
            lineup.append(post)

            counter += 1           

        # permutating to get possible outcomes
        results = []
        for i in lineup:
            for j in lineup:
                for k in lineup:
                    if i == j == k:
                        pass
                    elif i == j:
                        pass
                    elif i == k:
                        pass
                    elif j == k:
                        pass
                    else:
                        permu = permutations([i,j,k], 3)

                        for p in list(permu):
                            newpass = ''.join(str(p))

                            if newpass in results:
                                pass
                            else:
                                results.append(newpass)


    # a list of all the possible correct ombinations to win the game
    victory = [
    # rows
    "(1, 2, 3)",
    "(1, 3, 2)",
    "(2, 1, 3)",
    "(2, 3, 1)",
    "(3, 1, 2)",
    "(3, 2, 1)",

    "(4, 5, 6)",
    "(4, 6, 5)",
    "(5, 4, 6)",
    "(5, 6, 4)",
    "(6, 4, 5)",
    "(6, 5, 4)",

    "(7, 8, 9)",
    "(7, 9, 8)",
    "(8, 7, 9)",
    "(8, 9, 7)",
    "(9, 7, 8)",
    "(9, 8, 7)",

    # cols
    "(1, 4, 7)",
    "(1, 7, 4)",
    "(4, 1, 7)",
    "(4, 7, 1)",
    "(7, 4, 1)",
    "(7, 1, 4)",

    "(2, 5, 8)",
    "(2, 8, 5)",
    "(5, 2, 8)",
    "(5, 8, 2)",
    "(8, 5, 2)",
    "(8, 2, 5)",

    "(3, 6, 9)",
    "(3, 9, 6)",
    "(6, 3, 9)",
    "(6, 9, 3)",
    "(9, 3, 6)",
    "(9, 6, 3)",

    # dias
    "(1, 5, 9)",
    "(1, 9, 5)",
    "(5, 1, 9)",
    "(5, 9, 1)",
    "(9, 1, 5)",
    "(9, 5, 1)",

    "(3, 5, 7)",
    "(3, 7, 5)",
    "(5, 3, 7)",
    "(5, 7, 3)",
    "(7, 3, 5)",
    "(7, 5, 3)",
]
    
    wins = []

    for i in results:
        if i in victory:
            wins.append(i)
    
    return wins
    