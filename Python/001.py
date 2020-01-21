def total_of_multiple_3and5(n):
    total = 0
    for x in range(0, n ):
        if x % 3 == 0 or x % 5 == 0:
            total = total + x
    return total


if __name__ == '__main__':
    print(total_of_multiple_3and5(1000))
