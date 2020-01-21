def largest_prime_factor(n):
    factors = find_factors(n)
    prime_factors = []
    for x in factors:
        temp = find_factors(x)
        if len(temp) == 0:
            prime_factors.append(x)
    return max(prime_factors)


def find_factors(n):
    # find factors
    factors = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            factors.append(x)
            factors.append(int(n / x))
    return factors


if __name__ == '__main__':
    print(largest_prime_factor(600851475143))
