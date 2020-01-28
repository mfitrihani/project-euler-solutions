def name_scores():
    file = open("C:\\Users\\MAMPU\\\PycharmProjects\\\project-euler-solutions\\Python\\p022_names.txt")
    names = file.read().replace("\"", "").split(",")
    names.sort()
    total = 0
    for x in range(0, len(names)):
        temp = 0
        for y in names[x]:
            temp += ord(y) - 64
        total = total + temp*(x + 1)
    return total


if __name__ == '__main__':
    print(name_scores())
