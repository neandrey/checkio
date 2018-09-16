def to_encrypt(text, delta):

    S = str()
    for i in text:
        if i == ' ':
            S += i
            continue
        temp = delta
        result = ord(i)
        if temp > 0:
            while(temp):
                result += 1
                temp -= 1
                if result > 122:
                    result = 97
            S += chr(result)
#---------------------------------------
        if temp < 0:
            while(temp):
                result -= 1
                temp += 1
                if result < 97:
                    result = 122
            S += chr(result)

    return S


if __name__ == '__main__':
    print("Example:")
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")