def is_pandigital(n):
    n = [int(x) for x in list(str(n))]
    n.sort()
    return n == [1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    product = set()
    for x in range(1, 99):
        for y in range(1, 9999):
            temp = int(str(x*y) + str(x) + str(y))
            if is_pandigital(temp):
                product.add(x*y)
    print(sum(product))
