combi = []


def combination(a, b):
    if sum(b) > 200:
        return
    elif sum(b) == 200:
        combi.append(b)
    else:
        if len(b) == 0:
            temp_a = a.copy()
        else:
            temp_a = [x for x in a if x <= b[-1]]
        for x in temp_a:
            temp_b = b.copy()
            temp_b.append(x)
            combination(a, temp_b)


if __name__ == '__main__':
    combination([200, 100, 50, 20, 10, 5, 2, 1], [])
    print(combi)
    print(len(combi))
