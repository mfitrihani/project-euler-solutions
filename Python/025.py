def index_of_n_digits_fibonacci_sequence(n):
    sequence = [1, 1, 2]
    last = sequence[-1]
    while len(str(last)) < n:
        sequence.append(sequence[-1] + sequence[-2])
        last = sequence[-1]
    return len(sequence)


if __name__ == '__main__':
    print(index_of_n_digits_fibonacci_sequence(1000))
