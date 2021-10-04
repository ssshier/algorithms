def solve(lst):
    n = int(lst[0])
    find_lst = lst[1:1 + n]
    find_str = lst[-2]
    find_str_sorted = sorted([char for char in find_str])
    find_index = int(lst[-1])

    find_res = []
    for item in find_lst:
        if item != find_str and sorted([char for char in item]) == find_str_sorted:
            find_res.append(item)
    find_res.sort()
    print(len(find_res))
    print(find_res[find_index-1])


if __name__ == '__main__':
    while True:
        try:
            in_lst = input().split()
            solve(in_lst)
        except:
            break
