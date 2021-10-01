from collections import defaultdict


def solve(dt, index, val):
    dt[index] += val


if __name__ == '__main__':
    n = int(input())
    dt = defaultdict(int)
    for _ in range(n):
        index, val = map(int, input().split(' '))
        solve(dt, index, val)
    lst = [(key, val) for key, val in dt.items()]
    lst.sort(key=lambda item: item[0])
    for key, val in lst:
        print(key, val)
