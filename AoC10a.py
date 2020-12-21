f = open("jolts.txt")

joltageRat = []
for line in f:
    line = int(line)
    joltageRat.append(line)

joltageRat.sort()


diffCounts = {1:0,2:0,3:1}

lng = len(joltageRat)

prevNum = 0
i = 0
while i < lng:
    diff = joltageRat[i]-prevNum
    #print(diff)
    diffCounts[diff] = diffCounts.get(diff)+1
    prevNum = joltageRat[i]
    i+=1

print(diffCounts)

answer = diffCounts[1] * diffCounts[3]
print("The product of the number of 1 differences and the number of 3 differences is",answer)
