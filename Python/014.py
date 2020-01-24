import time
start_time = time.time()


def produce_collatz_sequence(number):
    sequence = [number]
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
        sequence.append(number)
    return sequence


def find_longest_collatz_sequence(maximum_starting_number):
    longest_sequence_number = 0
    max_sequence_length = 0
    for x in range(2, maximum_starting_number+1):
        sequence_length = len(produce_collatz_sequence(x))
        if sequence_length > max_sequence_length:
            longest_sequence_number = x
            max_sequence_length = sequence_length
    return longest_sequence_number


if __name__ == '__main__':
    print(find_longest_collatz_sequence(1000000))
    print(time.time()-start_time)
