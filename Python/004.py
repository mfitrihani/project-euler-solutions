def is_palindrome(n):
    temp = n
    r = 0
    while n > 0:
        r = r * 10
        r = r + n % 10
        n = int(n / 10)
    return temp == r


def give_max_palindrome(maximum_factors):
    palindromes = []
    for x in range(1, maximum_factors + 1):
        for y in range(1, maximum_factors + 1):
            if is_palindrome(x * y):
                palindromes.append(x * y)
    return max(palindromes)


if __name__ == '__main__':
    print(give_max_palindrome(999))
