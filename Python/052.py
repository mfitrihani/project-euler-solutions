if __name__ == '__main__':
    x = 1
    while True:
        if sorted(list(str(x))) == sorted(list(str(x*2))) == sorted(list(str(x*3))) == sorted(list(str(x*4))) == sorted(list(str(x*5))) == sorted(list(str(x*6))):
            break
        x += 1
    print(x)
