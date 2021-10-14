def tolong(st):
    lst = st.split('.')
    bin_st = '0b'
    for item in lst:
        bin_item = bin(int(item))[2:]
        bin_item = bin_item.rjust(8, '0')
        bin_st += bin_item
    return int(bin_st, 2)


def toip(st):
    bin_st = bin(int(st))[2:]
    bin_st = bin_st.rjust(32, '0')
    ip_nums = []
    for i in range(4):
        int_item = int('0b' + bin_st[i * 8:(i + 1) * 8], 2)
        ip_nums.append(str(int_item))
    return '.'.join(ip_nums)


if __name__ == '__main__':
    while True:
        try:
            print(tolong(input()))
            print(toip(input()))
        except:
            break
