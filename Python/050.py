def generate_prime_numbers(maximum):
    candidates = [True for x in range(0, maximum)]
    for x in range(2, int(maximum ** 0.5) + 2):
        if candidates[x]:
            i = x * x
            while i < maximum:
                candidates[i] = False
                i += x
    prime_numbers = []
    for x in range(2, maximum):
        if candidates[x]:
            prime_numbers.append(x)
    return prime_numbers


prime_numbers = generate_prime_numbers(1000000)


def get_prime_addition(n):
    summation = []
    index, start_index, total = 0, 0, 0
    while prime_numbers[index] < int(3*n/4):
        summation.append(prime_numbers[index])
        total += prime_numbers[index]
        if total == n:
            return summation
        elif total > n:
            total = 0
            summation.clear()
            start_index += 1
            index = start_index
        index += 1
    return []


if __name__ == '__main__':
    longest_addition = 0
    longest_addition_length = 0
    for x in prime_numbers:
        addition = get_prime_addition(x)
        if len(addition) > longest_addition_length:
            longest_addition_length = len(addition)
            longest_addition = x
    print(longest_addition)
