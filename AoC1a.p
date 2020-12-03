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
    print("Testing this number:")
    print(testnum1)
    testnum1 = int(testnum1)
    i = 0
    while i <= flist_len:
        testnum2 = flist[i-1]
        testnum2 = int(testnum2)
        ##print(testnum2)
        sum = testnum1 + testnum2
        if sum  == 2020:
            done = 1
            finalnum1 = testnum1
            finalnum2 = testnum2
            print("done")
            break
        else:
            i = i + 1

print(finalnum1, finalnum2)
product = finalnum1*finalnum2
print(product)
