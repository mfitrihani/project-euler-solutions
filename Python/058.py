# def produce_triangle_edge(n):
#     edges = [1]
#     addition = 2
#     x = 0
#     while x < n:
#         for y in range(0, 4):
#             edges.append(edges[len(edges) - 1] + addition)
#         addition += 2
#         x += 1
#     return edges


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
    prime_count = 0
    number_count = 1
    edge_count = 1
    edges = [1]
    addition = 2
    while True:
        for y in range(0, 4):
            edges.append(edges[len(edges) - 1] + addition)
            number_count += 1
            if is_prime(edges[len(edges) - 1]):
                prime_count += 1
        edge_count += 2
        addition += 2
        if prime_count/number_count < 0.1:
            print(edge_count)
            break
