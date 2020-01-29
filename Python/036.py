def find_double_base_palindromes(limit):
    values = []
    for x in range(1, limit + 1):
        if is_palindrome(x):
            if is_palindrome("{0:b}".format(x)):
                values.append(x)
    return values


def is_palindrome(n):
    li = list(str(n))
    temp = li.copy()
    li.reverse()
    return temp == li


if __name__ == '__main__':
    print(sum(find_double_base_palindromes(1000001)))
