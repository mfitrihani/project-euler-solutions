def power_five_of_digits(a):
    total = 0
    while a > 0:
        total = total + pow(a % 10, 5)
        a = a // 10
    return total


def find_fifth_power():
    values = []
    for x in range(2, 999999):
        if x == power_five_of_digits(x):
            values.append(x)
    return values


if __name__ == '__main__':
    print(sum(find_fifth_power()))
