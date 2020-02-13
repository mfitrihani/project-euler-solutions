def get_factors(n):
    factors = []
    for x in range(2, int(n**0.5) + 2):
        if n % x == 0 and x == n/x:
            factors.append(x)
        elif n % x == 0:
            factors.append(x)
            factors.append(int(n/x))
    return factors

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
    i = 646
    while True:
        is_consecutive = True
        for x in range(i, i + 4):
            factors = get_factors(x)
            prime_factors = [n for n in factors if is_prime(n)]
            if len(factors) < 4:
                i = x + 1
                is_consecutive = False
                break
            elif len(prime_factors) < 4:
                i = x + 1
                is_consecutive = False
                break
        if is_consecutive:
            print("The first of the 4 consecutive integers to have4 distinct prime factors is")
            print(i)
            break
