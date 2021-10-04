def solve(lst):
    dp = [1] * len(lst)
    for i in range(len(lst)):
        for j in range(i):
            if lst[j] < lst[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return dp


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            ss = list(map(int, input().split(' ')))
            left = solve(ss)
            right = solve(ss[::-1])[::-1]
            sum_s = []
            for i in range(len(left)):
                sum_s.append(left[i] + right[i] - 1)
            print(n-max(sum_s))
        except:
            break
