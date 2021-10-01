from collections import Counter


def solve(st, char):
    st = st.lower()
    counter = Counter(st)
    count = counter.get(char.lower())
    return count if count else 0


if __name__ == '__main__':
    print(solve(input(), input()))
