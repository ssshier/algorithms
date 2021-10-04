from collections import defaultdict


def solve(st):
    dt = defaultdict(int)
    for char in st:
        dt[char] += 1
    min_count = sorted(dt.values())[0]
    delete_chars = [key for key, val in dt.items() if val == min_count]
    for char in delete_chars:
        st = st.replace(char, '')
    return st


if __name__ == '__main__':
    while True:
        try:
            s = input()
            print(solve(s))
        except:
            break
