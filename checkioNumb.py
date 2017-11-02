def checkio(number):

    numb = 1
    string = str(number)
    print(string)
    for s in string:
        if s == '0':
            continue
        numb = numb * int(s)

    return numb


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
