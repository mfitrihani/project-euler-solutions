def elim_same_digit(x, y):
    x = list(str(x))
    y = list(str(y))
    i = 0
    while i < len(x):
        j = 0
        while j < len(y):
            if x[i] == y[j]:
                x.pop(i)
                y.pop(j)
                i, j = -1, 0
                break
            else:
                j += 1
        i += 1
    if len(x) == 0:
        x.append("0")
    if len(y) == 0:
        y.append("0")
    return [int("".join(x)), int("".join(y))]


if __name__ == '__main__':
    product_x = 1
    product_y = 1
    for x in range(10, 100):
        for y in range(x, 100):
            temp = elim_same_digit(x, y)
            if temp[1] == 0:
                continue
            if x / y == temp[0] / temp[1] and x != temp[0] and y != temp[1] and x % 10 != 0 and y % 10 != 0:
                print(str(x) + " / " + str(y))
                product_x *= temp[0]
                product_y *= temp[1]
    print(product_x)
    print(product_y)
