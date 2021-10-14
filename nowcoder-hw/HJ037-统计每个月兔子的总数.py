def solve(st):
    month = int(st)
    if month == 1:
        return 1
    elif month == 2:
        return 1

    total_one = 1
    total_two = 0
    total_three = 0

    for _ in range(1, month):
        total_three += total_two
        tmp = total_one
        total_one = total_three
        total_two = tmp
    total = total_one + total_two + total_three
    return total


if __name__ == '__main__':
    while True:
        try:
            print(solve(input()))
        except:
            break