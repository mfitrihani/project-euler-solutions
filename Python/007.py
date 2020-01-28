def find_nth_prime_number(n):
    prime_numbers = [2]
    number = 3
    while True:
        if len(prime_numbers) == n:
            return prime_numbers[len(prime_numbers)-1]
        if is_prime(number):
            prime_numbers.append(number)
        number += 2


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for x in range(2, int(n ** 0.5) + 2):
        if n % x == 0:
            return False
    return True


if __name__ == '__main__':
    print(find_nth_prime_number(10001))
