f = open("jolts.txt")

joltageRat = []
for line in f:
    line = int(line)
    joltageRat.append(line)

joltageRat.sort()

print(joltageRat)

lng = len(joltageRat)

print(lng)

countKey = {1:1,2:2,3:4,4:7,5:11,6:16}

diffList = []

#create a list of the difference between each number in the sequence. Should be 1s and 3s
prevNum = 0
i=0
while i < lng:
    diff = joltageRat[i]-prevNum
    diffList.append(diff)
    prevNum = joltageRat[i]
    i+=1

print(diffList)

#create a list of the number of 1s in a row. This will help determine possible combos
rawPosNums = []
i=0
oneCount = 0
while i < lng:
    if diffList[i] == 3:
        print(oneCount)
        rawPosNums.append(oneCount)
        oneCount = 0
        i+=1
        continue
    elif i == lng-1:
        rawPosNums.append(oneCount+1)
        oneCount = 0
        i+=1
    else:
        oneCount+=1
        i+=1

print(rawPosNums)

onesCount = {1:0,2:0,3:0,4:0,5:0}
#loop through rawPosNums to create a count of the number of times each 1s sequence appearances
for num in rawPosNums:
    if num == 0:
        continue
    onesCount[num] = onesCount.get(num)+1

print(onesCount)


numTwos = onesCount[2]
numThrees = onesCount[3]
numFours = onesCount[4]
numFives = onesCount[5]

print("Number of twos", numTwos)
print("Number of threes", numThrees)
print("number of fours", numFours)
total = (2**numTwos) * (4**numThrees) * (7**numFours)
print(total)
