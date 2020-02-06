def produce_spiral(size):
    box = [[1]]
    direction = "right"
    x = 2
    while x <= size * size:
        if direction == "right":
            direction = "down"
            for i in range(0, len(box)):
                box[i].append(x)
                x += 1
        elif direction == "down":
            direction = "left"
            temp = [i for i in range(x, x + len(box[0]))]
            temp.reverse()
            box.append(temp)
            x += len(box[0])
        elif direction == "left":
            direction = "up"
            for i in range(0, len(box)):
                box[len(box) - i - 1].insert(0, x)
                x += 1
        elif direction == "up":
            direction = "right"
            box.insert(0, [i for i in range(x, x + len(box[0]))])
            x += len(box[0])
    return box


if __name__ == '__main__':
    spiral = produce_spiral(1001)
    # total of diagonal numbers
    total = 0
    x, y = 0, 0
    while x < len(spiral[0]):
        total += spiral[y][x]
        total += spiral[y][len(spiral) - x - 1]
        x += 1
        y += 1
    total -= 1
    print(total)
