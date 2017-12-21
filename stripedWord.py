VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"
#--------------------------
import re
notWhite = re.compile('\W')
digit = re.compile('[0-9]')

#---------------------
def highFunc(text):
    """
    :param text: string simbol
    :return: high string simbol
    """
    return text.upper()
#--------------------------------
def whiteSymbol(text):
    """
    :param text - input string:
    :return: str without is symbols ,./ and other '\W'.
    """

    Str = str()
    for let in text:
        if notWhite.match(let):
            Str +=' '
        else:
            Str += let

    return Str

#--------------------------------
def counterWord(text):
    """
    :param
    input: text:
    temp:   temp - parametr to save a first word in string
    :return:
    counterWords - count word in string.
    """

    counterWords = 0

    while text:
        flagCounter = 0
        temp = text[:1]
        if temp[0] == '' or digit.search(temp[0]):
            text = text[1:]
            continue
        #---------------------------
        for i in temp[0]:
            if (len(temp[0]) == 1):
                break
            if ((i in VOWELS) and (flagCounter == -1)) or ((i in CONSONANTS) and (flagCounter == 1)):
                 break
            if (i in VOWELS) and (flagCounter == 1 or flagCounter == 0):
                flagCounter = -1
            if (i in CONSONANTS) and (flagCounter == -1 or flagCounter == 0):
                flagCounter = 1
        #-----------------------------
        else:
            counterWords += 1
        text = text[1:]

    return counterWords

#------------------------------------
def checkio(text):
    text = highFunc(text)
    text = whiteSymbol(text).strip(' ')
    text = text.split(' ')
    counterWords = counterWord(text)


    return counterWords

#-----------------------------------------
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
    assert checkio("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.") == 5
    assert checkio("1st 2a ab3er root rate") == 1
