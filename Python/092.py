def square_digit_sum(n):
    return sum(pow(int(x), 2) for x in str(n))


arrive_to_89 = {89}


def loop_arrive_89(n):
    loop = [n]
    while True:
        if n in arrive_to_89:
            for x in loop:
                arrive_to_89.add(x)
            return True
        elif n == 1:
            return False
        n = square_digit_sum(n)
        loop.append(n)


if __name__ == '__main__':
    count = 0
    for x in range(1, 10000001):
        if loop_arrive_89(x):
            count += 1
    print(count)
    # approximately 57 seconds
