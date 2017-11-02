#--------------------------------------
def lenFunct(l):
    l = l / 2
    lenData = (int(l))
    return lenData
#---------------------------
def checkio(data):
    lenData = len(data)
    data.sort()
    if lenData % 2 == 0:
        h = lenFunct(lenData)
        z = h-1
        return ((data[z] + data[h]) / 2)
    else:
        h = lenFunct(lenData)
        return data[h]
#--------------------------
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")