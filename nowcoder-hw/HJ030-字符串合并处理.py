def combine(st1, st2):
    return st1 + st2


def sort(st):
    evens = []
    odds = []
    for i in range(len(st)):
        if i % 2 == 0:
            evens.append(st[i])
        else:
            odds.append(st[i])
    evens.sort(key=lambda x: ord(x))
    odds.sort(key=lambda x: ord(x))
    res = ''
    for i in range(len(st)):
        if i % 2 == 0:
            res += evens.pop(0)
        else:
            res += odds.pop(0)
    return res


def change(st):
    res = ''
    hexs = "0123456789abcdefABCDEF"
    for char in st:
        if char in hexs:
            to2 = format(int(char, 16), 'b').rjust(4, '0')
            to16 = format(int(to2[::-1], 2), 'X')
            res += to16
        else:
            res += char
    return res


if __name__ == '__main__':
    while True:
        try:
            s1, s2 = input().split()
            print(change(sort(combine(s1, s2))))
        except:
            break
