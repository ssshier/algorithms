def solve(st: str):
    res = []
    item = ''
    for char in st:
        if char.isalpha():
            item += char
        else:
            res.append(' ')
            res.append(item)
            item = ''
    res.append(' ')
    res.append(item)
    res.reverse()
    return ''.join(res)


if __name__ == '__main__':
    print(solve(input()))
