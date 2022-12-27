#https://adventofcode.com/2022/day/13
from functools import cmp_to_key
import math
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = [list(map(eval, x.split("\n"))) for x in input.read().split("\n\n")]
    count = sum(idx+1 for idx, (x,y) in enumerate(data) if recr(x,y)<0)
    data = sorted([y for x in data for y in x]+[[[2]],[[6]]],key=cmp_to_key(recr))
    return count, math.prod([idx+1 for idx, x in enumerate(data) if x in ([[2]], [[6]])])

def recr(x,y):
    x,y = x if isinstance(x, list) else [x],y if isinstance(y, list) else [y]
    for x2,y2 in zip(x,y):
        if isinstance(x2, list) or isinstance(y2, list):
            diff = recr(x2,y2)
        else:
            diff = x2-y2
        if diff:
            return diff
    return len(x) - len(y)
