def factorial_digit_sum(n):
    factorial = 1
    while n > 0:
        factorial = factorial*n
        n -= 1
    digit_sum = 0
    while factorial > 0:
        digit_sum = digit_sum + factorial % 10
        factorial = factorial // 10
    return digit_sum


if __name__ == '__main__':
    print(factorial_digit_sum(100))