def produce_triangle_edge(n):
    edges = [1]
    addition = 2
    x = 0
    while x < n:
        for y in range(0, 4):
            edges.append(edges[len(edges) - 1] + addition)
        addition += 2
        x += 1
    return edges


def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(n**0.5) + 1):
            if n % x == 0:
                return False
        return True


if __name__ == '__main__':
    for x in range(1, 9999):
        triangle_edge = produce_triangle_edge(x)
        prime_triangle_edge = [x for x in triangle_edge if is_prime(x)]
        if len(prime_triangle_edge) / len(triangle_edge) < 0.1:
            print(1 + 2*(x-1))
            break
