import sys


def get_answer():
    s = sys.argv[1]
    answer = ''
    for word in s.split(sep=' '):
        answer += word[0]
    print(answer)


if __name__ == "__main__":
    get_answer()

