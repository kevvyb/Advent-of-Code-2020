f = open("q&a.txt")

answerList = []
for line in f:
    answerList.append(line)

#returns the number of unique appearances of letters in a single line
def letterCount(answerLine,alphCount):
    num_answers = 0
    if "a" in answerLine:
        alphCount["a"] = alphCount.get("a",0) + 1
    if "b" in answerLine:
        alphCount["b"] = alphCount.get("b",0) + 1
    if "c" in answerLine:
        alphCount["c"] = alphCount.get("c",0) + 1
    if "d" in answerLine:
        alphCount["d"] = alphCount.get("d",0) + 1
    if "e" in answerLine:
        alphCount["e"] = alphCount.get("e",0) + 1
    if "f" in answerLine:
        alphCount["f"] = alphCount.get("f",0) + 1
    if "g" in answerLine:
        alphCount["g"] = alphCount.get("g",0) + 1
    if "h" in answerLine:
        alphCount["h"] = alphCount.get("h",0) + 1
    if "i" in answerLine:
        alphCount["i"] = alphCount.get("i",0) + 1
    if "j" in answerLine:
        alphCount["j"] = alphCount.get("j",0) + 1
    if "k" in answerLine:
        alphCount["k"] = alphCount.get("k",0) + 1
    if "l" in answerLine:
        alphCount["l"] = alphCount.get("l",0) + 1
    if "m" in answerLine:
        alphCount["m"] = alphCount.get("m",0) + 1
    if "n" in answerLine:
        alphCount["n"] = alphCount.get("n",0) + 1
    if "o" in answerLine:
        alphCount["o"] = alphCount.get("o",0) + 1
    if "p" in answerLine:
        alphCount["p"] = alphCount.get("p",0) + 1
    if "q" in answerLine:
        alphCount["q"] = alphCount.get("q",0) + 1
    if "r" in answerLine:
        alphCount["r"] = alphCount.get("r",0) + 1
    if "s" in answerLine:
        alphCount["s"] = alphCount.get("s",0) + 1
    if "t" in answerLine:
        alphCount["t"] = alphCount.get("t",0) + 1
    if "u" in answerLine:
        alphCount["u"] = alphCount.get("u",0) + 1
    if "v" in answerLine:
        alphCount["v"] = alphCount.get("v",0) + 1
    if "w" in answerLine:
        alphCount["w"] = alphCount.get("w",0) + 1
    if "x" in answerLine:
        alphCount["x"] = alphCount.get("x",0) + 1
    if "y" in answerLine:
        alphCount["y"] = alphCount.get("y",0) + 1
    if "z" in answerLine:
        alphCount["z"] = alphCount.get("z",0) + 1
    return alphCount

#concatenate family answers into one line (familyLine) and store in the list familyAnswers

alphCount = dict()
totalCount = 0
count = 0
for line in answerList:
    if line == "\n":
        print(alphCount)
        print(count)
        for values in alphCount.values():
            if values == count:
                totalCount+=1
        count = 0
        alphCount = dict()
        continue
    if line == answerList[-1]:
        line = line.strip()
        line = str(line)
        alphCount = letterCount(line,alphCount)
        count+=1
        print(alphCount)
        print(count)
        for values in alphCount.values():
            if values == count:
                totalCount+=1
        count = 0
        alphCount = dict()
    line = line.strip()
    line = str(line)
    alphCount = letterCount(line,alphCount)
    count+=1

print("Total Count:",totalCount)
