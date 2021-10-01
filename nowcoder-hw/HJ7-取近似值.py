def solve(st: str):
    val1, val2 = st.split(".")
    if int(val2[0]) >= 5:
        return int(val1) + 1
    else:
        return int(val1)
    

if __name__ == '__main__':
    print(solve(input()))