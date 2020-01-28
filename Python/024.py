import itertools


def permute(n):
    permuted = list(itertools.permutations(n))
    strings = []
    for x in permuted:
        strings.append("".join(x))
    strings.sort()
    return strings


if __name__ == '__main__':
    print(permute("0123456789")[999999])
