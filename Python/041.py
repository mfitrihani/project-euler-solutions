from itertools import permutations
import time

current_time = time.time()
temp = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10))
palindrome_numbers = [int("".join([str(y) for y in x])) for x in temp]


def is_prime(n):
    if n == 2:
        return True
    else:
        for x in range(2, int(n ** 0.5) + 2):
            if n % x == 0:
                return False
        return True


if __name__ == '__main__':
    prime_numbers = []
    for x in palindrome_numbers:
        if is_prime(x):
            prime_numbers.append(x)
    print(prime_numbers)
    print(time.time() - current_time)
