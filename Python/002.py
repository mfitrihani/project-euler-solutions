def get_fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)


def total_even_fibonacci(n):
    total = 0
    control = 0
    fibonacci_number = 0
    while fibonacci_number < n:
        if fibonacci_number % 2 == 0:
            total = total + fibonacci_number
        control = control + 1
        fibonacci_number = get_fibonacci(control)
    return total


if __name__ == '__main__':
    print(total_even_fibonacci(4000000))
