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

#curNum is the broken Number

i = 0
sum = 0
done = 0
while i < lng:
    if done ==1:
        print("break")
        break
    sum = sum + int(xmas[i])
    j = i + 1
    while j < lng:
        sum = sum + int(xmas[j])
        #print(sum)
        if sum == curNum:
            print("The first index is",i)
            print("The second index is", j)
            print("The magic sum is",sum)
            done = 1
            break
        if sum > curNum:
            #print("The sum is greater:",sum)
            break
        j+=1
    i+=1
    sum = 0


finalSum = int(xmas[j+1])+int(xmas[i+1])
print("The sum is", finalSum)
finalSum2 = int(xmas[j])+int(xmas[i])
print(xmas[j])
print(xmas[i])
print("The sum is", finalSum2)
