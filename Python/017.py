import num2words


def count_words(minimum, maximum):
    total = 0
    for x in range(minimum, maximum+1):
        total = total + len(num2words.num2words(x).replace(" ", "").replace("-", ""))
    return total


if __name__ == '__main__':
    print(count_words(1, 1000))
