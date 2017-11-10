#------------------------
def fibonachi(s):
    if s == 0 or s == 1:
        return True
    i = 1
    h = 1
    while 1:

        z = i + h
        h = i
        i = z

        if s == z:
            print(z)
            return True

        if s < z:
            return False

#------------------------------

def checkio(opacity):
    const = 10000
    for i in range(4999):
        if fibonachi(i):
            const -= i
        else:
            const += 1
        if opacity == const:
            return i

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
    print('Good Work')
