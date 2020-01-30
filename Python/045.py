triangular_number = [x * (x + 1) / 2 for x in range(286, 100000)]


def find_triangular_number():
    for x in triangular_number:
        if is_pentagonal(x) and is_hexagonal(x):
            return x

def is_pentagonal(y):
    x = (1 + (1 + 24 * y) ** 0.5) / 6
    if x.is_integer() and x > 0:
        return True
    else:
        x = (1 - (1 + 24 * y) ** 0.5) / 6
        return x.is_integer() and x > 0


def is_hexagonal(y):
    x = (1 + (1 + 8 * y) ** 0.5) / 4
    if x.is_integer() and x > 0:
        return True
    else:
        (1 - (1 + 8 * y) ** 0.5) / 4
        return x.is_integer() and x > 0


if __name__ == '__main__':
    print(find_triangular_number())
