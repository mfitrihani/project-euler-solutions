# slow and with predetermined limit but i'm to lazy to make up another algorithm
def find_pythagorean_triplet_with_total_of(total_of_triplet):
    for a in range(1, 999):
        for b in range(a + 1, 999):
            for c in range(b + 1, 999):
                if c * c == a * a + b * b and a + b + c == total_of_triplet:
                    return [a, b, c]


if __name__ == '__main__':
    print(find_pythagorean_triplet_with_total_of(1000))
