#https://adventofcode.com/2022/day/1
def solve(file,index):
    with open(f"./inputs/{file}",'r') as input:
        return sum(sorted([sum(list(map(int,x.split("\n")))) for x in input.read().split("\n\n")[:-1]],reverse=True)[:index])
