
import re
#---------------------
def lowerLetter(text):
    return  text.lower()
#--------------------------
def removeSingle(text):
    L = []
    for tx in text:
        if re.match(r'[a-z]', tx):
            L.append(tx)
    return L
#---------------------------
def mostWantedLater(L):
    h = 1
    D = {}
    while True:
        if len(L) == 1:
            break
        simbol = L[0]
        #-------------
        for l in L[1]:
            if simbol == l:
                h += 1
                D[l] = h
            else:
                h = 1
            del L[0]
            break

    print(D)
    return D
#--------------------------

def checkio(text):
    text = lowerLetter(text)
    print(text)
    L = removeSingle(text)
    L.sort()
    L1 = L[:]
    text = mostWantedLater(L)
    if text == {}:
        return L1[0]
    else:
        cout = max(list(text.values()))
        letters = (list(text.keys()))
        L = (text.items())
        for t in L:
            if t[1] == cout:
                    return t[0]
#-----------------------------

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
