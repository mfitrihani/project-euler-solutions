def produce_amicable_number(maximum):
    amicable_numbers = []
    for x in range(1, maximum+1):
        temp = sum(find_proper_divisors(x))
        temp2 = sum(find_proper_divisors(temp))
        if x == temp2 and x != temp:
            amicable_numbers.append([x, temp])
    # sort
    for x in amicable_numbers:
        x.sort()
    # remove duplicate
    control = len(amicable_numbers)
    x = 1
    while x < control:
        if amicable_numbers[x] == amicable_numbers[x-1]:
            amicable_numbers.pop(x)
            control -= 1
        x += 1
    return amicable_numbers


def find_proper_divisors(n):
    divisors = []
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return divisors


if __name__ == '__main__':
    amicable_pairs = produce_amicable_number(10000)
    total = 0
    for x in amicable_pairs:
        for y in x:
            total += y
    print(total)
