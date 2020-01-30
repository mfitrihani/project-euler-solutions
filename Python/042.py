triangle_number = [1/2*x*(x + 1) for x in range(1, 101)]


def find_triangle_words():
    file = open("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\p042_words.txt")
    string = file.read()
    words = string.replace("\"", "").split(",")
    triangle_words = []
    for x in words:
        if is_triangular_words(x):
            triangle_words.append(x)
    return triangle_words


def is_triangular_words(n):
    total = 0
    for x in n:
        total = total + (ord(x) - 64)
    return total in triangle_number


if __name__ == '__main__':
    print(len(find_triangle_words()))
