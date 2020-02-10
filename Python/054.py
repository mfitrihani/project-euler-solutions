from itertools import cycle


def check_cards(n):
    royal_flush = ["10", "J", "Q", "K", "A"]
    value = 1000
    for x in royal_flush:
        if x not in n:
            value = 0
            break
    straight_flush = cycle(["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"])
    print(next(straight_flush))
    print(next(straight_flush))
    if value != 0:
        return value


if __name__ == '__main__':
    file = open("C:\\Users\\MAMPU\\PycharmProjects\\project-euler-solutions\\Python\\054.txt")
    hands = file.read().split("\n")
    # split into 2 players
    hands = [[x[:14], x[15:]] for x in hands]
    print(check_cards("10D JH QS KD AD"))
