def count_lattice_path(n, k):
    return permutation(n + k) / (permutation(k) * permutation(n))


def permutation(n):
    if n == 1:
        return 1
    else:
        total = 1
        while n > 1:
            total *= n
            n -= 1
        return total


if __name__ == '__main__':
    print(count_lattice_path(20, 20))
