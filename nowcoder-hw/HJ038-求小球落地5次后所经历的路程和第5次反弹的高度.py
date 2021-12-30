def solve(h: int):
    total = 0
    cur_h = h
    for _ in range(5):
        total += cur_h * 2
        cur_h = cur_h / 2
    total -= h
    
    return round(total, 6), round(cur_h, 6)


if __name__ == '__main__':
    while True:
        try:
            t, ch = solve(int(input()))
            print(t)
            print(ch)
        except:
            break