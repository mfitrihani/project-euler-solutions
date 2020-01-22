def find_greatest_adjacent_number(length):
    file = open("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\008.txt", "r")
    seek = 0
    max_product = 0
    while file.read(length) != "":
        file.seek(seek)
        temp = multiply_digits(int(file.read(length)))
        if temp > max_product:
            max_product = temp
        seek += 1
    file.close()
    return max_product


def multiply_digits(n):
    multiply = 1
    while n > 0:
        multiply = n % 10 * multiply
        n = int(n/10)
    return multiply


if __name__ == '__main__':
    print(find_greatest_adjacent_number(13))
