if __name__ == '__main__':
    total = 0
    for x in range(1, 1001):
        total = total + (x**x % 10000000000)
    print(total % 10000000000)