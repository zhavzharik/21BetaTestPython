import sys
import re


def check_line(text, check):
    iteration = 0
    for line in text:
        line = line.rstrip('\n')
        if len(line) == 32 and re.match(r'[0]{5}[^0]{1}', line):
            print(line, end="\n")
        iteration +=1
        if iteration == check:
            break


if __name__ == "__main__":
    number = int(sys.argv[1])
    check_line(sys.stdin, number)

