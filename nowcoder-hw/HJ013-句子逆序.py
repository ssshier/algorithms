def solve(st):
    lst = st.split(' ')
    lst.reverse()
    return " ".join(lst)


if __name__ == '__main__':
    print(solve(input()))
