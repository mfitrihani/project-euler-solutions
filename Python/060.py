import itertools


def generate_prime_numbers(limit):
    candidates = [True for x in range(0, limit + 1)]
    for x in range(2, int(limit ** 0.5) + 2):
        if candidates[x]:
            index = 2 * x
            while index < limit + 1:
                candidates[index] = False
                index += x
    prime_numbers = []
    for x in range(2, limit + 1):
        if candidates[x]:
            prime_numbers.append(x)
    return prime_numbers


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
    prime_numbers = generate_prime_numbers(200)
    sets_of_5primes = list(itertools.combinations(prime_numbers, 5))
    for x in sets_of_5primes:
        temp = list(itertools.permutations(x, 2))
        if all(is_prime(int(str(y[0]) + str(y[1]))) for y in temp):
            print(x)
            break
    # print(int(str(temp[0][0]) + str(temp[0][1])))
