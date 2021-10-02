import re


def solve(st):
    if len(st) <= 8:
        return False

    if re.findall(r'(.{3,}).*\1', st):
        return False

    class_count = 0
    if re.search('[A-Z]', st):
        class_count += 1
    if re.search('[a-z]', st):
        class_count += 1
    if re.search('[0-9]', st):
        class_count += 1
    if re.search('[^A-Za-z0-9]', st):
        class_count += 1
    if class_count < 3:
        return False

    return True


if __name__ == '__main__':
    while True:
        try:
            if solve(input()):
                print("OK")
            else:
                print("NG")
        except:
            break
