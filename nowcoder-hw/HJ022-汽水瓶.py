def solve(st):
    num = int(st)
    return num // 2


if __name__ == '__main__':
    while True:
        try:
            s = input()
            if s == '0':
                break
            print(solve(s))
        except:
            break
