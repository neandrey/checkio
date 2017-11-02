def verify_anagrams(first_word, second_word):
    S = (second_word.lower()).split(' ')
    S = list(('').join(S))
    print(S)

    L = (first_word.lower()).split(' ')
    L = list(('').join(L))
    print(L)

    for letter in L:
        if letter in S:
            S.remove(letter)
            L = L[1:]
            #print(S)
    if S != [] or L != []:
        return False
    else:
        return True
#---------------------------------------
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "hell") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"