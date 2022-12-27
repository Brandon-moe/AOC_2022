#https://adventofcode.com/2022/day/6
def solve(file,index):
    with open(f"./inputs/{file}","r") as f:
        data = list(f.read())
    return ([0]*(index-1)+list(map(lambda *x: len(set(x))==index,*[data[index-1:]]+[data[index-1-n:-n] for n in range(1,index)]))).index(True)+1
