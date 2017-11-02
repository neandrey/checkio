def checkio(data):
    i = 0
    h = 0
    m = 0
    res = list(data)
    if len(res) < 10:
        return False
    for r in res:
        if '0' <= r <= '9':
            i = 1
        elif 'a' <= r <= 'z':
            h = 1
        elif 'A' <= r <= 'Z':
            m = 1
    if i == 1 and h == 1 and m == 1:
        return  True
    else:
        return False


#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
