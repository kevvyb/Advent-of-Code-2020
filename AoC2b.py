f = open("password_policy.txt", "r")

#f = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

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

    polPass = 0
    print(pw[fstNum-1])
    print(let)
    if pw[fstNum-1] == let:
        polPass = polPass + 1

    print(pw[sndNum-1])
    if pw[sndNum-1] == let:
        polPass = polPass + 1

    if polPass == 1:
        totalcnt = totalcnt + 1
        print(totalcnt)


print(totalcnt)
