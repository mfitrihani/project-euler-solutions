def is_prime(n):
    factors = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            factors.append(x)
            factors.append(int(n / x))
    return len(factors) == 0


def total_of_prime(max_prime_number):
    total = 2
    number = 3
    while number < max_prime_number:
        if is_prime(number):
            total += number
        number += 2
    return total


def generate_prime_number(max_prime_number):
    candidate = []


if __name__ == '__main__':
    print(total_of_prime(2000000))
