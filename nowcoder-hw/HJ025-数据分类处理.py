def solve(i, r):
    r.sort()
    res = []
    for r_index in range(len(r)):
        res_i = []
        for i_index in range(len(i)):
            if r_index == 0 or (r_index > 0 and r[r_index] != r[r_index - 1]):
                if str(r[r_index]) in str(i[i_index]):
                    res_i.append(i_index)
                    res_i.append(i[i_index])
        if res_i:
            res_i.insert(0, len(res_i) // 2)
            res_i.insert(0, r[r_index])
            res.extend(res_i)
    res.insert(0, len(res))
    return ' '.join(map(str, res))


if __name__ == '__main__':
    while True:
        try:
            in_i = list(map(int, input().split()[1:]))
            in_r = list(map(int, input().split()[1:]))
            print(solve(in_i, in_r))
        except:
            break
