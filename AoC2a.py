f = open("password_policy.txt", "r")

#testList = ["1-3 a: abcde", "10-34 b: cdefg", "2-9 c: ccccccccc"]

totalcnt = 0
for pwpol in f:
    pwpol = str(pwpol)
    lng = len(pwpol)
    print(pwpol)
    colIndex = pwpol.index(":")
    dashIndex = pwpol.index("-")
    letIndex = colIndex-1
    let = pwpol[colIndex-1]
    fstNum = pwpol[0:dashIndex]
    fstNum = int(fstNum)
    sndNum = pwpol[(dashIndex+1):(letIndex-1)]
    sndNum = int(sndNum)
    pw = pwpol[colIndex+2:lng]
    print(pw)

    cnt = 0
    for l in pw:
        if l == let:
            cnt = cnt+1

    print(cnt)
    if cnt >= fstNum and cnt <=sndNum:
        totalcnt = totalcnt+1
        print("pass")


print(totalcnt)
