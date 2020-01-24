def sum_of_digits_from_file(file_path):
    file = open(file_path)
    digits = file.read().split("\n")
    total = 0
    for x in digits:
        total = total + int(x)
    return total


if __name__ == '__main__':
    print(sum_of_digits_from_file("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\013.txt"))