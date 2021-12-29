def solve(key: str, st: str) -> str:
    a_z = [chr(i) for i in range(65, 91)]
    s = []
    for char in key:
        if char.upper() not in s:
            s.append(char.upper())
    for char in a_z:
        if char not in s:
            s.append(char)
    res = ""
    for char in st:
        if char.isalpha():
            index = a_z.index(char.upper())
            res += s[index] if char.isupper() else s[index].lower()
        else:
            res += char
    return res


if __name__ == '__main__':
    while True:
        try:
            print(solve(input(), input()))
        except:
            break