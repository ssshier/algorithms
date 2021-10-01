def solve(lst):
    lst.sort(key=lambda x: x)
    return lst


if __name__ == '__main__':
    n = int(input())
    ls = [input() for _ in range(n)]
    res = solve(ls)
    for item in res:
        print(item)
