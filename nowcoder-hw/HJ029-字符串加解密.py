def encrypt(st):
    new_st = ''
    for char in st:
        if char.isdigit():
            if char == '9':
                new_st += '0'
            else:
                new_st += str(int(char) + 1)
        elif char.isupper():
            if char == 'Z':
                new_st += 'a'
            else:
                new_st += chr(ord(char) + 1).lower()
        elif char.islower():
            if char == 'z':
                new_st += 'A'
            else:
                new_st += chr(ord(char) + 1).upper()
    return new_st


def decrypt(st):
    new_st = ''
    for char in st:
        if char.isdigit():
            if char == '0':
                new_st += '9'
            else:
                new_st += str(int(char) - 1)
        elif char.isupper():
            if char == 'A':
                new_st += 'z'
            else:
                new_st += chr(ord(char) - 1).lower()
        elif char.islower():
            if char == 'a':
                new_st += 'Z'
            else:
                new_st += chr(ord(char) - 1).upper()
    return new_st


if __name__ == '__main__':
    while True:
        try:
            encrypt_st = input()
            decrypt_st = input()
            print(encrypt(encrypt_st))
            print(decrypt(decrypt_st))
        except:
            break
