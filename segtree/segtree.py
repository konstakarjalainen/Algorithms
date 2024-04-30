import sys

def printTree(array):
    tree = [array]
    branches = array
    while len(branches) > 1:
        i = 0
        upper_branches = []
        while i < len(branches):
            if i % 2 == 0:
                upper_branches.append(branches[i])
            else:
                upper_branches[i//2] += branches[i]
            i += 1
        branches = upper_branches
        tree.insert(0, upper_branches)
    print("Segment tree levels:")
    for level in tree:
        level_string = ""
        for val in level:
            level_string = f"{level_string} {val}"
        print(level_string)
    print()


def query(first, last, arr):
    start = first
    end = last
    print()
    print(f"Querying interval {first}...{last}")
    max_index = 1
    poweroftwo = len(arr)
    while poweroftwo > 0:
        max_index += poweroftwo
        poweroftwo = poweroftwo // 2
    level = arr[start:end+1]
    index_substr = len(arr)
    result = 0
    left = max_index - index_substr + start
    right = max_index - index_substr + end
    while len(level) > 0:
        print(f"  left and right positions: {left} {right}")
        i = 0
        upper_arr = []
        if left % 2 == 1 or len(level) == 1:
            val = level.pop(0)
            print(f"    updated result from {result} to {result+val} using S[{left}]={val}")
            result += val
            left += 1
        if right % 2 == 0 and len(level) > 0:
            val = level.pop()
            print(f"    updated result from {result} to {result+val} using S[{right}]={val}")
            result += val
            right -= 1
        while i < len(level):
            if i % 2 == 0:
                upper_arr.append(level[i])
            else:
                upper_arr[i//2] += level[i]
            i += 1
        index_substr += index_substr//2
        left = left // 2
        right = right // 2
        level = upper_arr
    
    print()
    print(f"Sum({first}...{last}) = {result}")


array_file = sys.argv[1]
command_file = sys.argv[2]

array_file = open(array_file, "r")
command_file = open(command_file, "r")
arr = []
for line in array_file:
    row = line.split()
    for num in row:
        arr.append(int(num))
n = 2
while len(arr) > n:
    n = n*2
for i in range(n-len(arr)):
    arr.append(0)
commands = []
for line in command_file:
    cmd, par1, par2 = line.split()
    commands.append((cmd, int(par1), int(par2)))

printTree(arr)

for command in commands:
    if command[0] == "query":
        query(command[1], command[2], arr)
    else:
        print()
        print(f"Updating V[{command[1]}] = {command[2]}")
        arr[command[1]] = command[2]
