def is_prime(n):
    if n <= 1:
        return True
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for x in range(5, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True


def find_factors(n):
    factors = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x == n/x:
                factors.append(x)
            else:
                factors.append(x)
                factors.append(n/x)
    factors.sort()
    factors.reverse()
    return factors


if __name__ == '__main__':
    for x in find_factors(600851475143):
        if is_prime(x):
            print(x)
            break
