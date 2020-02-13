def truncate_num(n):
    numbers = [n]
    n = str(n)
    for x in range(0, len(str(n)) - 1):
        numbers.append(int(n[:len(n) - 1 - x]))
        numbers.append(int(n[x + 1:]))
    return numbers


def generate_primes(limit):
    candidates = [True for x in range(0, limit + 1)]
    for x in range(2, len(candidates)):
        if candidates[x]:
            index = x*2
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


if __name__ == '__main__':
    primes_num = [i for i in generate_primes(1000000) if i > 10]
    truncatable_primes = []
    for x in primes_num:
        if all(is_prime(i) for i in truncate_num(x)):
            truncatable_primes.append(x)
    print(truncatable_primes)
    print(sum(truncatable_primes))
