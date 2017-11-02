def sum(res):
    f = 0
    for r in res:
        f += r
    return f
#------------------
def mul(array, i):
    f = i * array[-1]
    return f

#------------------
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if array == []:
        return 0;
    else:
        l = len(array)
        res = []
        for arr in range(l):
            if  arr % 2 == 0:
                res.append(array[arr])

        i = sum(res)
        f = mul(array, i)

        return f
#-------------------------------------------
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"