def smallest_divisible_number(division_range):
    number_of_succeed_division = 0
    number = division_range
    multiplication_factor = 1
    while True:
        for x in range(1, division_range + 1):
            if number % x == 0:
                number_of_succeed_division += 1
            else:
                multiplication_factor = min(find_factors(x))
                break
            if number_of_succeed_division == division_range:
                return number
        number_of_succeed_division = 0
        number = number*multiplication_factor


def find_factors(n):
    factors = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            factors.append(x)
            factors.append(int(n / x))
    factors.append(n)
    return factors


if __name__ == '__main__':
    print(smallest_divisible_number(20))
