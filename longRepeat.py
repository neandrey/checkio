
def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    if len(line) == 0:
        return 0
    i = 0
    L = []
    h = 1
    for li in line:
        i += 1
        if len(line) > i:
            if li == line[i]:
                h += 1
                print(li)
                continue
        L.append(h)
        h = 1
        print(L)


    i =max(L)
    return i

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('aa') == 2, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')