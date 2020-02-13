def is_1to9digit_pandigital(n):
    n = list(str(n))
    n.sort()
    return n == ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


if __name__ == '__main__':
    for y in range(1, 10000):
        x = 1
        temp = y*x
        while len(str(temp)) < 9:
            x += 1
            temp = int(str(temp) + str(y*x))
        if is_1to9digit_pandigital(temp):
            print("--------------")
            print("number = " + str(y))
            print("multiply by 1 to " + str(x))
            print("pandigital number = " + str(temp))
