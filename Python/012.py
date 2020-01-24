def find_factors(n):
    factors = []
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            factors.append(x)
            factors.append(int(n / x))
    return factors


def triangle_number(n):
    total = 0
    for x in range(1, n+1):
        total += x
    return total


if __name__ == '__main__':
    x = 1
    triangular_number = triangle_number(x)
    factors_of_triangular_number = find_factors(triangular_number)
    while len(factors_of_triangular_number) < 500:
        x += 1
        triangular_number = triangle_number(x)
        factors_of_triangular_number = find_factors(triangular_number)
    print(triangular_number)
