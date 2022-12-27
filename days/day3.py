#https://adventofcode.com/2022/day/3
import string
def solve(file,part):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().splitlines()
        if part=="a":
            return sum(map(lambda x: string.ascii_letters.index(list(set(x[:len(x)//2])&set(x[len(x)//2:]))[0])+1,data))
        return sum(map(lambda x: string.ascii_letters.index(list(set(x[0])&set(x[1])&set(x[2]))[0])+1,[data[i:i+3] for i in range(0,len(data),3)]))
