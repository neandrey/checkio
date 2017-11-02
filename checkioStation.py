#------------------------------------
def checkSum(expression):
    ch = 0
    for ex in expression:
        if (ex == '[' or ex =='{' or ex =='(' or ex ==')' or ex ==']' or ex =='}'):
            ch += 1
    return ch
#-------------------------------------
def convertList(expression):
    res = []
    for ex in expression:
        if ex == '(' or ex == '{' or ex == '[':
            res.append(ex)
        elif ((ex == ')' and res[-1] == '(')
              or (ex == ']' and res[-1] == '[')
              or (ex == '}' and res[-1] == '{')):
            res.pop()
        elif (('0' <= ex <= '9') or (ex == '+' or ex == '-' or ex == '/' or ex == '*')):
            pass
        #else:
        #    res = ex
        #   return res
    return res
#---------------------------
def checkio(expression):
    if (checkSum(expression) % 2) != 0:
        return False
    res1 = convertList(expression)
    if res1 == []:
        return True
    else:
        return False
#-----------------------------
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
    assert checkio("(((([[[{{{3}}}]]]]))))") == False
    assert checkio("(((1+(1+1))))]") == False