def replace_digit(index, number, replacement):
    number = list(str(number))
    replacement = list(str(replacement))
    for x in range(0, len(replacement)):
        number[x + index] = replacement[x]
    return int("".join(number))


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(n**0,5) + 1):
            if n % x == 0:
                return False
        return True


if __name__ == '__main__':
    print(replace_digit(0, 9999, 2222))
