import math
#--------------------------------
def checkio(numbers_array):
    numbers_array = list(numbers_array)
    l = (len(numbers_array))

    for i in range(l):
        for h in range(i + 1, l):
            if math.fabs(numbers_array[i]) > math.fabs(numbers_array[h]):
                temp = numbers_array[h]
                numbers_array[h] = numbers_array[i]
                numbers_array[i] = temp

    return numbers_array
#-------------------------------------------------

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)


    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"