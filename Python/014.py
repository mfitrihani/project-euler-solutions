import time

start_time = time.time()
sequence_count_table = {1: 1}


def calculate_collatz_sequence(number):
    if number in sequence_count_table:
        return sequence_count_table[number]
    elif number % 2 == 0:
        sequence_count = 1 + calculate_collatz_sequence(number / 2)
        sequence_count_table[number] = sequence_count
        return sequence_count
    else:
        sequence_count = 1 + calculate_collatz_sequence(3 * number + 1)
        sequence_count_table[number] = sequence_count
        return sequence_count


def find_longest_collatz_sequence(maximum_starting_number):
    longest_sequence_number = 0
    max_sequence_length = 0
    for x in range(int(maximum_starting_number / 2), maximum_starting_number + 1):
        sequence_length = calculate_collatz_sequence(x)
        if sequence_length > max_sequence_length:
            longest_sequence_number = x
            max_sequence_length = sequence_length
    return longest_sequence_number


if __name__ == '__main__':
    print(find_longest_collatz_sequence(1000000))
    print(time.time() - start_time)
