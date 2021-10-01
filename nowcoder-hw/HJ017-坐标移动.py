import re


def solve(st: str):
    lst = st.split(';')
    use_lst = []
    for item in lst:
        if re.match('^[ADSW]{1}\d+$', item):
            use_lst.append(item)
    pos = [0, 0]
    for item in use_lst:
        if item[0] == 'A':
            pos[0] -= int(item[1:])
        if item[0] == 'D':
            pos[0] += int(item[1:])
        if item[0] == 'S':
            pos[1] -= int(item[1:])
        if item[0] == 'W':
            pos[1] += int(item[1:])
    return f"{pos[0]},{pos[1]}"


if __name__ == '__main__':
    print(solve(input()))
