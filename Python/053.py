from math import factorial

if __name__ == '__main__':
    count = 0
    for n in range(1, 101):
        for r in range(1, n + 1):
            if factorial(n) / (factorial(r)*factorial(n-r)) > 1000000:
                count += (n - 2*r + 1)
                break
    print(count)
