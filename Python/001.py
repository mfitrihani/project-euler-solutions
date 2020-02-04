if __name__ == '__main__':
    multiple_3or5 = [x for x in range(0, 1000) if x % 3 == 0 or x % 5 == 0]
    print(sum(multiple_3or5))
