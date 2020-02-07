def check_cards(n):
    value = 0
    royal_flush = ["10", "J", "Q", "K", "A"]
    value = 1000
    for x in royal_flush:
        if n.find(x) == -1:
            value = 0
            break
    return value


if __name__ == '__main__':
    file = open("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\054.txt")
    hands = file.read().split("\n")
    # split into 2 players
    hands = [[x[:14], x[15:]] for x in hands]
    print(hands)
    print(check_cards("10D JH QS KD AD"))
