#https://adventofcode.com/2022/day/2
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        if part == "a":
            return sum(list(map(lambda x: 3*((ord(x.split(" ")[1])-ord(x.split(" ")[0])+2)%3)+ord(x.split(" ")[1])-87,input.read().splitlines())))
        return sum(list(map(lambda x: 3*((ord(x.split(" ")[1])-88)%3)+(ord(x.split(" ")[1])-87+ord(x.split(" ")[0])+2)%3+1,input.read().splitlines())))
