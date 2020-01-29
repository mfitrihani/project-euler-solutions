import time

perimeter = {}


def produce_triangular_number(maximum):
    triangular_numbers = []
    for x in range(1, maximum + 1):
        for y in range(x, maximum + 1):
            for z in range(y, maximum + 1):
                if (x + y + z) > maximum:
                    continue
                if (x * x + y * y) == z * z:
                    triangular_numbers.append([x, y, z])
    return triangular_numbers


if __name__ == '__main__':
    current_time = time.time()
    triangular_numbers = produce_triangular_number(1000)
    # count perimeter
    for x in triangular_numbers:
        if sum(x) in perimeter:
            perimeter.update({sum(x): perimeter.get(sum(x)) + 1})
        else:
            perimeter[sum(x)] = 1
    print(perimeter)
    # find key with highest value
    v = list(perimeter.values())
    k = list(perimeter.keys())
    print(k[v.index(max(v))])
    print(time.time() - current_time)
