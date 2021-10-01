def solve(st):
    res = ''
    for i in range(len(st)-1, -1, -1):
        if st[i] not in res:
            res += st[i]
    return res


if __name__ == '__main__':
    print(solve(input()))
 