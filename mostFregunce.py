def most_frequent(data):
    """
        determines the most frequently occurring string in the sequence.
    """
    D = dict()
    i = 0
    for d in data:
        if d in D:
            i += 1
        D[d] = i
    print(D)

    L = sorted(D.items(), key=lambda x : x[1], reverse=True)
    print(L)
    return L[0][0]


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_frequent([
        'a', 'b', 'c',
        'a', 'b',
        'a'
    ]) == 'a'

    assert most_frequent(['a', 'a', 'bi', 'bi', 'bi']) == 'bi'
    print('Done')