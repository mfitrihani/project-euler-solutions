import itertools


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(3, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True


if __name__ == '__main__':
    candidates = list(itertools.product([x for x in range(-1000, 1000)], [x for x in range(-1000, 1001)]))
    biggest_prime = 0
    biggest_ab = []
    for x in candidates:
        temp = 0
        n = 0
        while True:
            if is_prime(n * n + x[0] * n + x[1]):
                temp += 1
            else:
                break
            n += 1
        if temp > biggest_prime:
            biggest_ab.clear()
            biggest_ab.append(x)
            biggest_prime = temp
    print(biggest_ab)
