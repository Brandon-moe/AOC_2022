#https://adventofcode.com/2022/day/14
from itertools import product
def solve(file,part1=False):
    with open(f"./inputs/{file}",'r') as input:
        rocks = set(sum(sum([[list(map(tuple,product(range(min(x[i][0],x[i+1][0]),max(x[i][0],x[i+1][0])+1),range(min(x[i][1],x[i+1][1]),max(x[i][1],x[i+1][1])+1)))) for i in range(len(x)-1)] for x in list(map(lambda x: [list(map(int,i.split(","))) for i in x], [x.split(" -> ") for x in input.read().splitlines()]))],[]),[]))
    cave = [["." for x in range(min([0]+[x[0] for x in rocks]),max([1000]+[x[0] for x in rocks])+1)] for y in range(min([0]+[x[1] for x in rocks]),max([x[1] for x in rocks])+1)]
    cave = [["#" if (idx2,idx) in rocks else val2 for idx2,val2 in enumerate(val)] for idx,val in enumerate(cave)]
    if not part1:
        cave.append(["." for x in range(len(cave[0]))])
        cave.append(["#" for x in range(len(cave[0]))])
    while True:
        sand_moving = True
        if not "." == cave[0][500]:
            break
        cave[0][500] = "O"
        current_idx = [500,0]
        while sand_moving:
            if part1:
                if current_idx[1] >= max([x[1] for x in rocks]):
                    return sum(x.count("O") for x in cave)-1
            xpos = filter(lambda x: 0<=x<=len(cave[0]),[current_idx[0]-1,current_idx[0],current_idx[0]+1])
            options = [cave[current_idx[1]+1][i] for i in xpos]
            if "." == options[1]:
                cave[current_idx[1]+1][current_idx[0]] = "O"
                new_idx = [current_idx[0],current_idx[1]+1]
            elif "." == options[0]:
                cave[current_idx[1]+1][current_idx[0]-1] = "O"
                new_idx = [current_idx[0]-1,current_idx[1]+1]
            elif "." == options[2]:
                cave[current_idx[1]+1][current_idx[0]+1] = "O"
                new_idx = [current_idx[0]+1,current_idx[1]+1]
            else:
                break
            cave[current_idx[1]][current_idx[0]] = "."
            current_idx = new_idx
    return sum(x.count("O") for x in cave) + part1
