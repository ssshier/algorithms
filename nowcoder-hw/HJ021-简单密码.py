def solve(st):
    new_st = ''
    for char in st:
        if char.isdigit():
            new_st += char
        elif char.isupper():
            if char != 'Z':
                new_st += chr(ord(char.lower()) + 1)
            else:
                new_st += 'a'
        else:
            if char in 'abc':
                new_st += '2'
            elif char in 'def':
                new_st += '3'
            elif char in 'ghi':
                new_st += '4'
            elif char in 'jkl':
                new_st += '5'
            elif char in 'mno':
                new_st += '6'
            elif char in 'pqrs':
                new_st += '7'
            elif char in 'tuv':
                new_st += '8'
            elif char in 'wxyz':
                new_st += '9'
    return new_st


if __name__ == '__main__':
    while True:
        try:
            print(solve(input()))
        except:
            break
