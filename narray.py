import numpy as np

def translate_matrix(length, matrix):
	arr = []
	for x in range(length):
		arr.append(list(matrix[x]))
	#print(arr)
	return arr


def return_answ(ret):
	s1 = str()
	for x in ret:
		for y in x:
			s1 += y
	return s1
		

def recall_password(cipher_grille, ciphered_password):
    length = (len(cipher_grille))
    matrixA = translate_matrix(length, cipher_grille)
    matrixB = translate_matrix(length, ciphered_password)
    M1 = list()
    #print(length)    

    while range(length): 
    	matrixA = np.array(matrixA)
    	matrixB = np.array(matrixB)
    	#print(matrixB)
    	M1.append(matrixB[matrixA == 'X'])
    	matrixA = np.rot90(matrixA, k=-1)
    	length -= 1


    return return_answ(M1) 


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
