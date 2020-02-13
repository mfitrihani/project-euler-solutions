def generate_primes(limit):
    candidates = [True for x in range(0, limit + 1)]
    for x in range(2, len(candidates)):
        if candidates[x]:
            index = x * 2
            while index < len(candidates):
                candidates[index] = False
                index += x
    prime_numbers = []
    for x in range(2, len(candidates)):
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


def is_goldbach(n):
    if n <= 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        prime_index = 0
        i = 1
        temp = prime_numbers[prime_index] + 2*pow(i, 2)
        while prime_numbers[prime_index] < n:
            if temp == n:
                return True
            elif temp > n:
                prime_index += 1
                i = 1
            else:
                i += 1
            temp = prime_numbers[prime_index] + 2 * pow(i, 2)
        return False


prime_numbers = generate_primes(100000)

if __name__ == '__main__':
    candidates = [x for x in range(9, 100000, 2) if not is_prime(x)]
    for x in candidates:
        if not is_goldbach(x):
            print(x)
            break
