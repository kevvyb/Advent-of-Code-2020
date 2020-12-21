f = open("XMAs.txt")

xmas = []
for line in f:
    xmas.append(line)

def prevSum(xmas, lineNum):
    nums = []
    i = lineNum

    while i < lineNum+25:
        #print("i is", i)
        j = lineNum+1

        while j < lineNum+25:
            #print("j is", j)
            #print(xmas[i])
            #print(xmas[j])
            inum = int(xmas[i])
            jnum = int(xmas[j])
            number = (jnum+inum)
            #print("Sum is:", number)
            nums.append(number)
            j+=1
        i+=1
    #print(nums)
    return nums

lng = len(xmas)

startNum = 25
while startNum < lng:
    curNum = int(xmas[startNum])
    prevSums = prevSum(xmas, startNum-25)
    #print("Previous Sums:")
    #print(prevSums)
    if curNum in prevSums:
        startNum +=1
        continue
    else:
        print("The broken number is:", curNum)
        break
    startNum +=1
