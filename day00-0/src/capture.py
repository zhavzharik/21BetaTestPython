import sys


def check_pattern(image, star):
    for i in range(0, 3):
        if image[i][0] == image[i][4] == star:
            check = 'True'
        else:
            check = 'False'
            break
        if image[1][1] == image[1][3] == image[2][2] == star:
            check = 'True'
        else:
            check = 'False'
            break
    return check


def check_others(image, star):
    others = []
    for i in range(0, 3):
        for j in range(0, 5):
            if image[i][j] != star and others.count(image[i][j]) == 0:
                others.append(image[i][j])
    if len(others) == 6:
        check = 'True'
    else:
        check = 'False'
    return check


def check_input(text):
    iteration = 0
    image = []
    for line in text:
        line = line.rstrip('\n')
        if len(line) == 5:
            star = line[0]
            image.append(line)
            flag = 'True'
            iteration += 1
        else:
            flag = 'Error'
            break
    if iteration == 3:
        flag = check_pattern(image, star)
        if flag == 'True':
            flag = check_others(image, star)
    else:
        flag = 'Error'
    return flag


if __name__ == "__main__":
    answer = check_input(sys.stdin)
    print(answer)
