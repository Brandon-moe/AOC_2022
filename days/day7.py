#https://adventofcode.com/2022/day/7
import re
class Tree:
    def __init__(self,parent=None,files=0):
        self.children = {}
        self.parent = parent
        self.files = files

def solve(file):
    with open(f"./inputs/{file}",'r') as input:
        data = input.read().replace("\n"," ").split("$ ")[2:]
    root = Tree()
    cd = root
    nodelist=[root]
    for line in data:
        if line[:2] == "cd":
            new_directory = line.split(" ")[1]
            if new_directory == "..":
                cd = cd.parent
            elif new_directory in cd.children.keys():
                cd = cd.children[new_directory]
            else:
                cd.children[new_directory] = Tree(parent=cd)
                cd = cd.children[new_directory]
                nodelist.append(cd)
        if line[:2] == "ls":
            line = line.split(" ")[1:]
            cd.files = sum(map(lambda x: int(re.findall("^[0-9]*", x)[0]), filter(lambda x: x[:3]!="dir",[x for x in [" ".join(line[i:i+2]) for i in range(0,len(line),2)] if x])))
    counter = sum(map(lambda x: x if x<=100000 else 0 ,map(check_directory_size,nodelist)))
    deletion = min(x for x in map(lambda x: x if x>=check_directory_size(root)-40000000 else 0 ,map(check_directory_size,nodelist)) if x!=0)
    return counter,deletion

def check_directory_size(node):
    if node.children == {}:
        return node.files
    return node.files + sum(map(lambda x: check_directory_size(x),list(node.children.values())))
