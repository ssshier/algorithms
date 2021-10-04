def isprime(num):
    if num <= 3:
        return True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find(odd, visited, choose, evens):
    for j, even in enumerate(evens):
        if isprime(odd + even) and not visited[j]:
            visited[j] = True
            if choose[j] == 0 or find(choose[j], visited, choose, evens):
                choose[j] = odd
                return True
    return False


def solve(nums):
    count = 0
    odds, evens = [], []
    for num in nums:
        if num % 2:
            odds.append(num)
        else:
            evens.append(num)
    choose = [0] * len(evens)
    for odd in odds:
        visited = [False] * len(evens)
        if find(odd, visited, choose, evens):
            count += 1
    return count


if __name__ == '__main__':
    while True:
        try:
            n = int(input())
            nums = list(map(int, input().split()))
            print(solve(nums))
        except:
            break
