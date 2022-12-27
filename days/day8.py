#https://adventofcode.com/2022/day/8
import numpy as np
def visibility(data,reverse=False,part1=True):
    visible_trees,stack = [-1 for i in data],[]
    for idx, val in (reversed(list(enumerate(data))) if reverse else enumerate(data)):
        while len(stack) > 0 and data[stack[-1]] <= val:
            index = stack.pop()
            visible_trees[index] = (val if part1 else idx)
        stack.append(idx)
    return visible_trees

def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = [[int(i) for i in list(line)] for line in input.read().splitlines()]
        right,down,left,up = [visibility(row) for row in data],[*zip(*[visibility(row) for row in [*zip(*data)]])],[visibility(row,True) for row in data],[*zip(*[visibility(row,True) for row in [*zip(*data)]])]
        count = sum([1 if min(x) == -1 else 0 for x in np.dstack((right,down,left,up)).reshape(len(data)*len(data[0]),4).tolist()])
        right = [i-iy if i>0 else len(data[0])-iy-1 for ix, row in enumerate([visibility(row,part1=False) for row in data]) for iy, i in enumerate(row)]
        down = [i-ix if i>0 else len(data)-ix-1 for ix, row in enumerate([*zip(*[visibility(row,part1=False) for row in [*zip(*data)]])]) for iy, i in enumerate(row)]
        left = [iy-i if i>0 else iy for ix, row in enumerate([visibility(row,True,False) for row in data]) for iy, i in enumerate(row)]
        up = [ix-i if i>0 else ix for ix, row in enumerate([*zip(*[visibility(row,True,False) for row in [*zip(*data)]])]) for iy, i in enumerate(row)]
        return count, max([w*x*y*z for w,x,y,z in zip(right,down,left,up)])
