#-----------------------------
def pawns_index(pawns):
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1
        col = ord(p[0]) - 97
        pawns_indexes.add((row, col))
        #print(pawns_indexes)
    return pawns_indexes
#----------------------------
def find_paws_plus(p):
    col = (p[0]) + 1
    row1 = (p[1]) + 1
    return (col, row1)
#---------------------
def find_paws_minus(p):
    col = (p[0]) + 1
    row2 = (p[1]) - 1
    return (col, row2)
#-----------------------------------
def safe_index(paws):
    find_paw = set()
    for p in paws:
        find_paw.add(find_paws_plus(p))
        find_paw.add(find_paws_minus(p))
    #print(find_paw)
    return find_paw
#------------------------
def safe_pawns(pawns):
    pawns = pawns_index(pawns)
    find_paw = safe_index(pawns)
    f = find_paw & pawns
    #print(f)
    return len(f)
#------------------------
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1