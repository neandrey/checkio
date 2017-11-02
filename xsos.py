def listConvert(game_result):
    List = []
    for i in game_result:
        L = list(i)
        List.append(L)
    return List
#---------------------------
def logicFunct(L, S):
    h = 0
    while h < 3:
        count_1 = 0
        count_2 = 0
        i = 0
        while i < 3:
            if L[h][i] == S:
                count_1 += 1
                if count_1 == 3:
                    return True
            if L[i][h] == S:
                count_2 += 1
                if count_2 == 3:
                    return True
            i += 1
        h += 1
    if ((L[0][0] == S and L[1][1] == S and L[2][2] == S) or
        L[0][2] == S and L[1][1] == S and L[2][0] == S):
        return True

    return False

#----------------------------
def checkio(game_result):
    print(game_result)
    L = listConvert(game_result)
    # c X
    S = 'X'
    if logicFunct(L,S):
        return 'X'
    #c O
    S = 'O'
    if logicFunct(L, S):
        return 'O'
    else:
        return 'D'
#--------------------------------

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"