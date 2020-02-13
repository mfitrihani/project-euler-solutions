import decimal

if __name__ == '__main__':
    temp = "01"
    for x in range(2, 200000):
        temp += str(x)
    print(int(temp[1]) * int(temp[10]) * int(temp[100]) * int(temp[1000]) * int(temp[10000]) * int(temp[100000]) * int(temp[1000000]))
