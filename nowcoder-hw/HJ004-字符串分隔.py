def solve(st):
    index = 0
    while True:
        p = st[index:index+8]
        if p:
            p += "0" * (8 - len(p))
            print(p)
            index += 8
        else:
            break
        
        
if __name__ == '__main__':
    while True:
        try:
            solve(input())
        except:
            break
