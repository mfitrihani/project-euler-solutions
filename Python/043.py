from itertools import permutations
temp = list(permutations("0123456789", 10))
pandigital_numbers = [x for x in temp if x[0] != "0"]


if __name__ == '__main__':
    # filter
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[1], x[2], x[3]))) % 2 == 0]
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[2], x[3], x[4]))) % 3 == 0]
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[3], x[4], x[5]))) % 5 == 0]
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[4], x[5], x[6]))) % 7 == 0]
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[5], x[6], x[7]))) % 11 == 0]
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[6], x[7], x[8]))) % 13 == 0]
    pandigital_numbers = [x for x in pandigital_numbers if int("".join((x[7], x[8], x[9]))) % 17 == 0]
    # combine into integer
    pandigital_numbers = [int("".join(x)) for x in pandigital_numbers]
    print(sum(pandigital_numbers))
