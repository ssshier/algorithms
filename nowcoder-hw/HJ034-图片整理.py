def solve(st):
    return ''.join(sorted(st, key=lambda x: ord(x)))


if __name__ == '__main__':
    while True:
        try:
            print(solve(input()))
        except:
            break
