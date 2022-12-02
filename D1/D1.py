# iter through file creatiung lists of list based on if blank line
import itertools


def per_section(it, is_delimiter=lambda x: x.isspace()):
    ret = []
    for line in it:
        if is_delimiter(line):
            if ret:
                yield ' '.join(ret)
                ret = []
        else:
            ret.append(line.rstrip())
    if ret:
        yield ' '.join(ret)
        
lol = []
with open("input.txt") as f:
    s = list(per_section(f))
    lol = [[int(j) for j in i.split(' ')] for i in s]

summed = [sum(i) for i in lol]
print(max(summed))