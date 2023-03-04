#String split and join

def split_and_join(line):
    # write your code here
    r = line.split()
    re = "-".join(r)
    return re

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)