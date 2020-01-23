matrix = []
matrix_temp = []


def text_to_matrix(directory):
    file = open(directory)
    string = file.read()
    char = [(s.split(" ")) for s in string.split("\n")]
    global matrix, matrix_temp
    matrix = [[int(y) for y in x] for x in char]
    matrix_temp = matrix.copy()


def find_greatest_adjacent_number(current_position):
    global matrix
    next_position = current_position.copy()
    highest = 0
    highest_position = []
    for x in range(-1, 2):
        next_position[0] = current_position[0] + x
        for y in range(-1, 2):
            next_position[1] = current_position[1] + y
            if matrix[next_position[1]][next_position[0]] > highest and next_position != current_position and next_position[0] >= 0 and next_position[1] >= 0:
                highest = matrix[next_position[1]][next_position[0]]
                highest_position = next_position.copy()
    return highest_position


def find_consecutive_adjacent_number(consecutive, current_position):
    positions = []
    matrix[current_position[1]][current_position[0]] = 0
    positions.append(current_position)
    for x in range(0, consecutive-1):
        current_position = find_greatest_adjacent_number(current_position)
        positions.append(current_position)
        matrix[current_position[1]][current_position[0]] = 0
    return positions


if __name__ == '__main__':
    text_to_matrix("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\011.txt")
    print(find_consecutive_adjacent_number(4, [0, 0]))
    print([max(x) for x in matrix])
