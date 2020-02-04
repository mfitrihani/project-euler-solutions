def generate_prime_numbers(minimum, maximum):
    candidates = [True for x in range(0, maximum)]
    for x in range(2, int(maximum ** 0.5) + 2):
        if candidates[x]:
            i = x * x
            while i < maximum:
                candidates[i] = False
                i += x
    prime_numbers = []
    for x in range(minimum, maximum):
        if candidates[x]:
            prime_numbers.append(x)
    return prime_numbers


prime_numbers = generate_prime_numbers(1000, 9999)


def find_permutation():
    potential_triplet = []
    for x in prime_numbers:
        if (x + 3330) in prime_numbers and (x + 6660) in prime_numbers:
            potential_triplet.append([x, x+3330, x+6660])
    permutation_triplet = []
    for x in potential_triplet:
        digit_1 = list(str(x[0]))
        digit_1.sort()
        digit_2 = list(str(x[1]))
        digit_2.sort()
        digit_3 = list(str(x[2]))
        digit_3.sort()
        if digit_1 == digit_2 == digit_3:
            permutation_triplet.append(x)
    return permutation_triplet


if __name__ == '__main__':
    print(find_permutation())
