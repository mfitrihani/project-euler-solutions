def circular(n):
    values = []
    n = str(n)
    for x in range(0, len(n)):
        n = n[len(n) - 1:] + n[0: len(n) - 1]
        values.append(int(n))
    return values


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
    circular_prime = []
    for x in range(1, 1000000):
        if all(is_prime(i) for i in circular(x)):
            circular_prime.append(x)
    print(len(circular_prime))
