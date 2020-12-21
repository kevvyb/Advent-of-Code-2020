f = open("vgame.txt")

vgameIns = []
for line in f:
    vgameIns.append(line)

def getCode(line):
    words = line.split()
    return words[0]

def getNum(line):
    words = line.split()
    return words[1]

#store the lines used in linesUsed. If a number comes up again, we stop
linesUsed = []
accel = 0

lineNum = [0]

for numLine in lineNum:
    numLine = int(numLine)
    line = vgameIns[numLine]
    print(line)
    inst = getCode(line)
    instNum = getNum(line)
    instNum = int(instNum)
    if inst == "acc":
        accel = accel + instNum
        newNum = numLine + 1
    if inst == "nop":
        newNum = numLine + 1
    if inst == "jmp":
        newNum = numLine + int(getNum(line))
    if newNum in lineNum:
        print("New number:",newNum)
        print(lineNum)
        break
    lineNum.append(newNum)
    print(newNum)

print(accel)
