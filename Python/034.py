from math import factorial


def digit_factorials():
    values = []
    for x in range(145, 99999):
        digits = break_into_digits(x)
        factored = [factorial(y) for y in digits]
        if sum(factored) == x:
            values.append(x)
    return values


def break_into_digits(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n//10
    return digits


if __name__ == '__main__':
    print(sum(digit_factorials()))