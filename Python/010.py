def generate_prime_number(max_prime_number):
    candidate = [True for x in range(0, max_prime_number)]
    for i in range(2, int(max_prime_number**0.5) + 2):
        if candidate[i]:
            j = i*i
            x = 1
            while j < max_prime_number:
                candidate[j] = False
                j = i*i + x*i
                x += 1
    prime_numbers = []
    for x in range(0, len(candidate)):
        if candidate[x]:
            prime_numbers.append(x)
    return prime_numbers


if __name__ == '__main__':
    print((generate_prime_number(2000000)))
