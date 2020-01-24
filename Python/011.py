from copy import copy, deepcopy

matrix = []
matrix_temp = []


def text_to_matrix(directory):
    file = open(directory)
    string = file.read()
    char = [(s.split(" ")) for s in string.split("\n")]
    global matrix
    global matrix_temp
    matrix = [[int(y) for y in x] for x in char]
    matrix_temp = deepcopy(matrix)


def find_greatest_adjacent_number(current_position):
    global matrix
    next_position = current_position.copy()
    highest = -1
    highest_position = []
    for x in range(-1, 2):
        next_position[0] = current_position[0] + x
        for y in range(-1, 2):
            next_position[1] = current_position[1] + y
            if next_position != current_position and next_position[0] >= 0 and next_position[1] >= 0 and next_position[
                0] < len(matrix) and \
                    next_position[1] < len(matrix[0]):
                if matrix[next_position[1]][next_position[0]] > highest:
                    highest = matrix[next_position[1]][next_position[0]]
                    highest_position = next_position.copy()
    return highest_position


def find_consecutive_adjacent_number(consecutive, current_position):
    positions = []
    matrix[current_position[1]][current_position[0]] = 0
    positions.append(current_position)
    for x in range(0, consecutive - 1):
        current_position = find_greatest_adjacent_number(current_position)
        positions.append(current_position)
        matrix[current_position[1]][current_position[0]] = 0
    return positions


def repeat_and_compare():
    max_product = 1
    product = 1
    current_position = []
    max_product_positions = []
    for x in range(0, len(matrix[0])):
        for y in range(0, len(matrix)):
            current_position = find_consecutive_adjacent_number(4, [x, y])
            for z in current_position:
                product = product * matrix_temp[z[1]][z[0]]
                print(current_position)
            if product > max_product:
                max_product = product
                max_product_positions = current_position
            product = 1
    return max_product_positions


if __name__ == '__main__':
    text_to_matrix("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\011.txt")
    print(repeat_and_compare())
