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


def get_prime_addition_length(n):
    index, start_index, total, length = 0, 0, 0, 0
    while total != n:
        total += prime_numbers[index]
        length += 1
        if prime_numbers[index] >= n or start_index > 3:
            return 1
        elif total > n:
            length = 0
            total = 0
            start_index += 1
            index = start_index
        else:
            index += 1
    return length


if __name__ == '__main__':
    longest_addition = 0
    longest_addition_length = 0
    for x in prime_numbers:
        temp = get_prime_addition_length(x)
        if temp > longest_addition_length:
            longest_addition_length = temp
            longest_addition = x
    print(longest_addition)
