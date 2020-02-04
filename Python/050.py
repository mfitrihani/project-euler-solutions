import time

current_time = time.time()
prime_numbers = []


def generate_prime_numbers(maximum):
    candidates = [True for x in range(0, maximum)]
    for x in range(2, int(maximum ** 0.5) + 2):
        if candidates[x]:
            i = x * x
            while maximum > i:
                candidates[i] = False
                i += x
    for x in range(2, maximum):
        if candidates[x]:
            prime_numbers.append(x)


def find_consecutive_prime_sum(n):
    start, end = 0, 0
    summation = 2
    while summation != n:
        if summation > n:
            summation = summation - prime_numbers[start]
            start += 1
        elif summation < n:
            end += 1
            summation = summation + prime_numbers[end]
    return [prime_numbers[x] for x in range(start, end + 1)]


if __name__ == '__main__':
    generate_prime_numbers(100000)
    longest_prime = 0
    max_length = 0
    for x in prime_numbers:
        summation = find_consecutive_prime_sum(x)
        if len(summation) > max_length:
            longest_prime = x
            max_length = len(summation)
    print(longest_prime)
    print(find_consecutive_prime_sum(longest_prime))
    print(time.time() - current_time)
