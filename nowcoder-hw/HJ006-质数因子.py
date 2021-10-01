def solve(num):
    lst = []
    i = 2
    while num != 1:
        if num % i == 0:
            lst.append(i)
            num = num // i
        else:
            if i > int(num**0.5):
                lst.append(num)
                break
            else:
                i += 1
    return " ".join(map(str, lst)) + " "


if __name__ == "__main__":
    print(solve(int(input())))
