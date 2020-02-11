import decimal


def find_recurring(denominator):
    if is_power(denominator, 2) or is_power(denominator, 5) or denominator == 2 or denominator == 5:
        return 0
    elif is_prime(denominator):
        test = decimal.Decimal(1/denominator)
        print(test)
        test = str(test)[2:]
        index = 0
        for x in range(1, len(test)):
            if test[x] == test[0]:
                index = x
                break
        return test[:index]


def is_power(x, y):
    if y == 1:
        return x == 1
    elif x == 1:
        return y == 1
    else:
        pow = 1
        while pow < x:
            pow *= y
        return pow == x


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True


if __name__ == '__main__':
    print(find_recurring(17))
