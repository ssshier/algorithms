def solve(a: str):
    bc = 0
    if a == a[::-1]:
        print(len(a))
    else:
        for i in range(len(a)):
            if i - bc >= 1 and a[i - bc - 1:i + 1] == a[i - bc - 1:i + 1][::-1]:
                bc += 2
            elif i - bc >= 0 and a[i - bc:i + 1] == a[i - bc:i + 1][::-1]:
                bc += 1
        print(bc)


if __name__ == '__main__':
    while True:
        try:
            solve(input())
        except:
            break
