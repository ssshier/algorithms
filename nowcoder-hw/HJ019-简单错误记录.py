from collections import OrderedDict

file_map = OrderedDict()


def solve(st):
    file_path, line = st.split(' ')
    file_name = file_path.split('\\')[-1][-16:]
    new_name = f'{file_name}.{line}'
    if file_map.get(new_name):
        file_map[new_name] += 1
    else:
        file_map[new_name] = 1


if __name__ == '__main__':

    while True:
        try:
            s = input()
            solve(s)
        except:
            break
    lst = [(key.split('.')[0], key.split('.')[1], value) for key, value in file_map.items()]
    for x, y, z in lst[-8:]:
        print(x, y, z)
