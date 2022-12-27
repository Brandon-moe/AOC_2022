#https://adventofcode.com/2022/day/5
def solve(file,index):
    with open(f"./inputs/{file}","r") as f:
        data = f.read().splitlines()
    crates,instructions = ["".join(x)[:-1].strip(" ")[::-1] for x in list(map(list, zip(*data[:data.index("")])))[1::4]],[list(map(int,x.split(" ")[1:6:2])) for x in data[data.index("")+1:]]
    for inst in instructions:
        crates[inst[2]-1] += crates[inst[1]-1][len(crates[inst[1]-1]) - inst[0]:][::index]
        crates[inst[1]-1] = crates[inst[1]-1][:len(crates[inst[1]-1]) - inst[0]]
    return "".join( [x[-1] for x in crates])
