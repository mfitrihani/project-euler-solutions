from itertools import permutations
import time

current_time = time.time()


def produce_prime_palindrome_numbers():
    temp = []
    tem = []
    for x in range(1, 10):
        tem.append(x)
        temp = temp + list(permutations(tem, x))
    palindrome_numbers = [int("".join([str(y) for y in x])) for x in temp]
    # filter for prime numbers
    prime_numbers = []
    for x in palindrome_numbers:
        if is_prime(x):
            prime_numbers.append(x)
    return prime_numbers


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        for x in range(2, int(n ** 0.5) + 2):
            if n % x == 0:
                return False
        return True


if __name__ == '__main__':
    print(produce_prime_palindrome_numbers())
    print(time.time() - current_time)
