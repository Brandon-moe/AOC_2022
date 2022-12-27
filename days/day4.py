#https://adventofcode.com/2022/day/4
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = [map(lambda x:set(range(int(x.split("-")[0]),int(x.split("-")[1])+1)),y) for y in [list(x) for x in zip(*[x.split(",") for x in input.read().splitlines()])]]
    if part == "a":
        return sum(map(lambda x,y: x<=y or y<=x,data[0],data[1]))
    return sum(map(lambda x,y: len(x&y)>0,data[0],data[1]))
