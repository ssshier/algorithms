def solve(n, primary, annex):
    dp = [0] * (n + 1)
    for key in primary:
        w, v = [], []
        w.append(primary[key][0])  # 1、主件
        v.append(primary[key][0] * primary[key][1])
        if key in annex:  # 存在附件
            w.append(w[0] + annex[key][0][0])  # 2、主件+附件1
            v.append(v[0] + annex[key][0][0] * annex[key][0][1])
            if len(annex[key]) > 1:  # 附件个数为2
                w.append(w[0] + annex[key][1][0])  # 3、主件+附件2
                v.append(v[0] + annex[key][1][0] * annex[key][1][1])
                w.append(w[0] + annex[key][0][0] + annex[key][1][0])  # 4、主件+附件1+附件2
                v.append(v[0] + annex[key][0][0] * annex[key][0][1] + annex[key][1][0] * annex[key][1][1])
        for j in range(n, -1, -10):  # 物品的价格是10的整数倍
            for k in range(len(w)):
                if j - w[k] >= 0:
                    dp[j] = max(dp[j], dp[j - w[k]] + v[k])
    return dp[n]


if __name__ == '__main__':
    # todo: rewrite
    n, m = map(int, input().split())
    primary, annex = {}, {}
    for i in range(1, m + 1):
        x, y, z = map(int, input().split())
        if z == 0:
            primary[i] = [x, y]
        else:
            if z in annex:
                annex[z].append([x, y])
            else:
                annex[z] = [[x, y]]
    print(solve(n, primary, annex))
