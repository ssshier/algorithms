def solve(st):
    az = []
    res = []
    for char in st:
        if char.isalpha():
            az.append(char)
        res.append(char)
    az.sort(key=lambda x: x.lower())
    i = 0
    for index, char in enumerate(res):
        if char.isalpha():
            res[index] = az[i]
            i += 1

    return ''.join(res)


if __name__ == '__main__':
    while True:
        try:
            print(solve(input()))
        except:
            break
