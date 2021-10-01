def solve(st: str):
    count = 0
    for i in str(bin(int(st))):
        if i == '1':
            count += 1
    return count


if __name__ == '__main__':
    print(solve(input()))