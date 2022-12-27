#https://adventofcode.com/2022/day/9
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().splitlines()
    knots = [[0,0] for x in range(part)]
    visited = set()
    dir = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    for line in data:
        for its in range(int(line.split(" ")[1])):
            knots[0] = [x+y for x,y in zip(knots[0],[x for x in dir[line.split(" ")[0]]])]
            for i in range(1,len(knots)):
                if not (knots[i-1][0] == knots[i][0] or knots[i-1][1] == knots[i][1]) and abs(knots[i-1][0]-knots[i][0])+abs(knots[i-1][1]-knots[i][1])>2:
                    knots[i] = [x+y for x,y in zip(knots[i],[y-x if abs(x-y)==1 else (1 if y>x else -1) for x,y in zip(knots[i],knots[i-1])])]
                new_tail = [y-1 if x<y else y if x==y else y+1 for x,y in zip(knots[i],knots[i-1])]
                ranges = [range(knots[i][x],new_tail[x]+1) if new_tail[x]>knots[i][x] else range(new_tail[x],knots[i][x]+1) for x in [0,1]]
                knots[i] = new_tail
            visited |= set([(x,y) for x in ranges[0] for y in ranges[1]])
    return len(visited)
