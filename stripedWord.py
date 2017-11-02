VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"

import re
#---------------------
def lowerLetter(text):
    """
    :param text: string simbol
    :return: lower string simbol
    """
    return text.lower()
#--------------------------
def removeSingleAndCountWord(text):
    '''
    :param text: string simbol
    :return: L->[], world - count word
    '''
    world = 0
    L = []
    for tx in text:
        z = text.index(tx)
        if tx == ' ' and re.match(r'[a-z]', text[z+1]):
            world += 1
        if re.match(r'[a-z\s]', tx):
            L.append(tx)
    return L, world
#---------------------------
def checkFunction(L, t1, t2):
    '''
    :param L:   data simbol
    :param t1:  test arraySimbol1
    :param t2:  test arraySimbol2
    :return:    True or False
    '''
    i = 0
    try:
        while (True):
            if L[i+1] == ' ':

            if(L[i] in t1) == (L[i+1] in t1) or (L[i] in t2) == (L[i+1] in t2):
                return False
            i += 1
    except TypeError:
        print('hello')



#--------------------------------
def checkio(text):
    t1 = lowerLetter(VOWELS)
    t2 = lowerLetter(CONSONANTS)
    text = lowerLetter(text)
    L, world = removeSingleAndCountWord(text)
    print(L, world)
    if checkFunction(L, t1, t2):
        return world
    else:
        return 0


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"