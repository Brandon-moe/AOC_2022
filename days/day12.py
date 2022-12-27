#https://adventofcode.com/2022/day/12
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = [list(x) for x in input.read().splitlines()]
    start_idx = list(filter(lambda x:x,[[idx,val.index("S")] if "S" in val else "" for idx,val in enumerate(data)]))[0]
    data[start_idx[0]][start_idx[1]] = "a"
    x = len(bfs(data, start_idx)) - 1
    return x,min([x]+[len(bfs(data, start_idx))-1 for start_idx in list(filter(lambda x:x,[[idx,val.index("a")] if "a" in val else "" for idx,val in enumerate(data)]))])

def bfs(data, current_idx):
    q = [[(current_idx[1],current_idx[0])]]
    traversed = set(tuple(current_idx))
    while q:
        path = q.pop(0)
        x, y = path[-1]
        if data[y][x] == "E":
            return path
        e = ord(data[y][x])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(data[0]) and 0 <= y2 < len(data) and (x2, y2) not in traversed:
                e2 = ord(data[y2][x2]) if data[y2][x2] != "E" else ord("z")
                if e2 <= e + 1:
                    q.append(path + [(x2, y2)])
                    traversed.add((x2, y2))
