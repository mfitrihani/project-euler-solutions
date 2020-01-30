pentagonal_numbers = [int(x * (3 * x - 1) / 2) for x in range(1, 10000)]


def find_pentagonal():
    x = 1
    for x in range(0, len(pentagonal_numbers)):
        for y in range(0, x):
            if is_pentagonal((pentagonal_numbers[x] + pentagonal_numbers[y])) and is_pentagonal(abs(pentagonal_numbers[x] - pentagonal_numbers[y])):
                return [pentagonal_numbers[x], pentagonal_numbers[y]]


def is_pentagonal(y):
    x = (1 + (1 + 24 * y) ** 0.5) / 6
    if x.is_integer() and x > 0:
        return True
    else:
        x = (1 - (1 + 24 * y) ** 0.5) / 6
        return x.is_integer() and x > 0


if __name__ == '__main__':
    print(find_pentagonal())
