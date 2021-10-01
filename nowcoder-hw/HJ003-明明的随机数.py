def solve(lst):
    return sorted(list(set(lst)))


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            lst = [int(input()) for _ in range(n)]
            res = solve(lst)
            for i in res:
                print(i)
        except:
            break
