f = open("expense.txt", "r")

flist = []
for num in f:
    flist.append(num)

flist_len = len(flist)
print(flist_len)

done = 0
for testnum1 in flist:
    if done == 1:
        break
    ##print("Testing this number:")
    ##print(testnum1)
    testnum1 = int(testnum1)
    ##get the next number in the file, convert to integer
    i = 0
    while i <= flist_len:
        testnum2 = flist[i-1]
        testnum2 = int(testnum2)
        j=0
        ##print(i)
        #print(j)
        while i <= (flist_len-j-2):
            #print(i+j)
            testnum3 = flist[i+j]
            testnum3 = int(testnum3)
            sum = testnum1 + testnum2 + testnum3
            if sum == 2020:
                done = 1
                finalnum1 = testnum1
                finalnum2 = testnum2
                finalnum3 = testnum3
                print("done")
                break
            else:
                j = j + 1
        i = i + 1


print(finalnum1, finalnum2, finalnum3)
product = finalnum1*finalnum2*finalnum3
print(product)
