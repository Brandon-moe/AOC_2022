#https://adventofcode.com/2022/day/10
def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = [x for y in [[x,"'"+x] if x[0]=="a" else [x] for x in input.read().splitlines()] for x in y]
    signal = [sum(map(lambda x: int(x.split(" ")[1]),filter(lambda x: x[0]=="'",data[max(0,i):40+i]))) for i in range(-21,219,40)]
    output = ["█" if y in [i%40-1,i%40,i%40+1] else " " for i,y in zip(range(240),[sum(map(lambda x: int(x.split(" ")[1]),filter(lambda x: x[0]=="'",data[:i])))+1 for i in range(240)])]
    print("\n".join(["".join(output[x:40+x]) for x in range(0,240,40)]))
    return signal[0]*720+signal[1]*700+signal[2]*640+signal[3]*540+signal[4]*400+signal[5]*220+720
