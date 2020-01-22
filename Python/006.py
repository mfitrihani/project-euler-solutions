import math


def difference_of_squares_of_1_to_n_number_and_square_of_n(n):
    return math.pow(sum([x for x in range(1, n + 1)]), 2) - sum([x * x for x in range(1, n + 1)])


if __name__ == '__main__':
    print(difference_of_squares_of_1_to_n_number_and_square_of_n(100))
