import math


def distinct_power(a, b):
    values = []
    for x in range(2, a + 1):
        for y in range(2, b + 1):
            values.append(int(math.pow(x, y)))
    values.sort()
    # remove duplicates
    x = 1
    while x < len(values):
        if values[x] == values[x-1]:
            values.pop(x-1)
        else:
            x += 1
    return len(values)


if __name__ == '__main__':
    print(distinct_power(100, 100))
