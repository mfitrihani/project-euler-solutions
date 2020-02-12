import decimal
import itertools

decimal.getcontext().prec = 10000
finite = list(itertools.product([pow(5, x) for x in range(0, 5)], [pow(2, x) for x in range(0, 11)]))
finite = [x[0]*x[1] for x in finite]
finite = [x for x in finite if x <= 500]


def find_recurring(denominator):
    # return 0 for finite decimal point which is when the the denominator is 2^x*5^y
    if denominator in finite:
        return ""
    else:
        test = decimal.Decimal(decimal.Decimal(1) / decimal.Decimal(denominator))
        test = str(test)[2:]
        start, end = 0, 1
        compare = test[start:end]
        while compare != test[end:end + len(compare)] or compare != test[end + len(compare): end + len(compare)*2] or compare != test[end + 2*len(compare): end + len(compare)*3]:
            if end == len(test):
                start += 1
                end = start + 1
            else:
                end += 1
            compare = test[start:end]
        return compare


if __name__ == '__main__':
    max_length = 0
    max_number = 0
    for x in range(2, 1000):
        temp = len(find_recurring(x))
        if temp > max_length:
            max_number = x
            max_length = temp
    print(max_number)
    print(max_length)
