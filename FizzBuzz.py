def fizz_buzz(y):

    if y % 15 == 0:
        return "FizzBuzz"
    elif y % 5 == 0:
        return "Buzz"
    elif y % 3 == 0:
        return "Fizz"
    else:
        return y
