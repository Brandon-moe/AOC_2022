#https://adventofcode.com/2022/day/15
import re
def solve(file,debug=False):
    row_index = (2000000 if not debug else 10)
    with open(f"./inputs/{file}",'r') as input:
        data =  list(map(lambda x:[int(y) for y in x],[re.findall("-?[0-9]+",x) for x in input.read().splitlines()]))
    beacons,sensors = [(x[2],x[3]) for x in data],[(x[0],x[1],abs(x[0]-x[2])+abs(x[1]-x[3])) for x in data]
    x = [sorted(list(filter(lambda x:x[0]<x[1], [(x[0]-x[2]+abs(x[1]-target),1+x[0]+x[2]-abs(x[1]-target)) for x in sensors])),key=lambda y:y[0]) for target in range(row_index*2)]
    positions = max(x[row_index][i][1] for i in range(len(x[row_index])))-x[row_index][0][0]-len(list(filter(lambda x: x[1] == row_index,set(beacons))))
    for idx,val in enumerate(x):
        current_max = val[0][1]
        for idx2,val2 in enumerate(val):
            if val2[0]-current_max > 0:
                return positions, idx+(4000000*(val2[0]-1))
            current_max = max(current_max,val2[1])
