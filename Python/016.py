def sum_digits(n):
    r = 0
    while n:
        n, remainder = divmod(n, 10)
        r += remainder
    return r


if __name__ == '__main__':
    print(sum_digits(2**1000))
