def popular_words(text, words):
    S = ''
    l_digit = []
    #заменяем '\n', '\t', ',', '.' на ' '
    for s in text:
        if s == '\n' or s == '\t' or s == ',' or s == '.':
            S += ' '
        else:
            S += s

    text = (S.lower()).split(' ')

    while(words):
        i = words.pop()
        h = 0
        for s in text:
            if i == s:
                h += 1
        l_digit.append([i, h])

    D = dict(l_digit)
    return D


if __name__ == '__main__':
    assert popular_words('''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
''', ['i', 'was', 'three']) == {
        'i': 4,
        'was': 3,
        'three': 0
    }

    print("Coding complete? Click 'Check' to earn cool rewards!")
