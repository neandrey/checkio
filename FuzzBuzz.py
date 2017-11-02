def checkio(number):
    if number % 5 == 0 and number % 3 == 0:
        number = "Fizz Buzz"
    elif number % 5 == 0:
        number = "Buzz"
    elif number % 3 == 0:
        number = "Fizz"

    return str(number)

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz"
    assert checkio(5) == "Buzz"
    assert checkio(7) == "7"
