def is_abundant_numb(n):
    total = 0
    for x in range(2, int(n ** 0.5) + 1):
        if n % x == 0:
            if x == n / x:
                total += x
            else:
                total += x
                total += n / x
        if total > n:
            return True
    return total > n


if __name__ == '__main__':
    abundant_numbers = [x for x in range(1, 28200) if is_abundant_numb(x)]
    # represented by its index
    not_sum_of_2abundant_num = [True for x in range(0, 28200)]
    for x in range(0, len(abundant_numbers)):
        for y in range(x, len(abundant_numbers)):
            if abundant_numbers[x] + abundant_numbers[y] < len(not_sum_of_2abundant_num):
                not_sum_of_2abundant_num[abundant_numbers[x] + abundant_numbers[y]] = False
    # find total
    total = 0
    for x in range(0, len(not_sum_of_2abundant_num)):
        if not_sum_of_2abundant_num[x]:
            total += x
    print(total)
