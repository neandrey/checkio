def count_words(text, words):
    count = 0
    text = text.lower()
    rec = set(text.split(' '))
    print(rec)
    for i in words:
        flag = 0
        for j in rec:
            if (j.find(i)) != -1 and flag == 0:
                count += 1
                flag = 1

    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
