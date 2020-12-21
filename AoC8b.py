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
lines = len(vgameIns)
i=0
newNum = 0
while i < lines:
    line = vgameIns[i]
    inst = getCode(line)

    accel = 0
    numLine = 0
    lineNum = [0]
    linesUsed = []
    for numLine in lineNum:

        numLine = int(numLine)
        line = vgameIns[numLine]
        #print(line)
        inst = getCode(line)
        instNum = getNum(line)
        instNum = int(instNum)
        if numLine == i:
            if inst == "nop":
                newNum = numLine + instNum
            elif inst == "jmp":
                newNum = numLine + 1
            elif inst == "acc":
                accel = accel + instNum
                newNum = numLine + 1

        elif inst == "acc":
            accel = accel + instNum
            newNum = numLine + 1
        elif inst == "nop":
            newNum = numLine + 1
        elif inst == "jmp":
            newNum = numLine + instNum

        if newNum in lineNum:
            #print("New number:",newNum)
            #print(lineNum)
            break
        lineNum.append(newNum)
        #print(newNum)
        #print(newNum)
        if newNum == lines:
            print("good", accel)

            break
    i+=1
print(accel)
