def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_lychrel(n):
    x = 0
    while x < 50:
        temp = n + int(str(n)[::-1])
        if is_palindrome(temp):
            return False
        else:
            n = temp
        x += 1
    return True


if __name__ == '__main__':
    print(len([x for x in range(1, 10001) if is_lychrel(x)]))
