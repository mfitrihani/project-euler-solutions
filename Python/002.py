def get_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for x in range(1, n):
            temp = a + b
            a = b
            b = temp
        return b


if __name__ == '__main__':
    total_even_fibo = 0
    index = 0
    fibo = 0
    while fibo < 4000000:
        if fibo % 2 ==0:
            total_even_fibo += fibo
        index += 1
        fibo = get_fibonacci(index)
    print(total_even_fibo)
