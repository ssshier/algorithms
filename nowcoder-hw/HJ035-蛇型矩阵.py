def solve(st):
    n = int(st)
    cur_num = 1
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            res[i - j][j] = cur_num
            cur_num += 1
    for item in res:
        print(' '.join(map(str, filter(lambda x: x != 0, item))))


if __name__ == '__main__':
    while True:
        try:
            solve(input())
        except:
            break
