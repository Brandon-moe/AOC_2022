#https://adventofcode.com/2022/day/11
import re, math
def solve(file,its):
    with open(f"./inputs/{file}",'r') as input:
        monkeys = [[re.findall("[0-9]+",x.split("\n")[1]),x.split("\n")[2].split("= ")[1],x.split("\n")[3].split(" ")[-1],x.split("\n")[4][-1],x.split("\n")[5][-1],0] for x in input.read().split("\n\n")]
        for i in range(its):
            for monkey in monkeys:
                monkey[0] = [eval(monkey[1].replace("old",str(x)))//3 if its==20 else eval(monkey[1].replace("old",str(x)))%math.prod(map(int,[x[2] for x in monkeys])) for x in monkey[0]]
                monkeys[int(monkey[3])][0] += [x for x in monkey[0] if not int(x)%int(monkey[2])]
                monkeys[int(monkey[4])][0] += [x for x in monkey[0] if int(x)%int(monkey[2])]
                monkey[5]+=len(monkey[0])
                monkey[0] = []
    return max([x[5] for x in monkeys])*max(filter(lambda x : x != max([x[5] for x in monkeys]),[x[5] for x in monkeys]))
