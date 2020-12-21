f = open("q&a.txt")

answerList = []
for line in f:
    answerList.append(line)

#returns the number of unique appearances of letters in a single line
def unique_answers(answerLine):
    num_answers = 0
    if "a" in answerLine:
        num_answers+=1
    if "b" in answerLine:
        num_answers+=1
    if "c" in answerLine:
        num_answers+=1
    if "d" in answerLine:
        num_answers+=1
    if "e" in answerLine:
        num_answers+=1
    if "f" in answerLine:
        num_answers+=1
    if "g" in answerLine:
        num_answers+=1
    if "h" in answerLine:
        num_answers+=1
    if "i" in answerLine:
        num_answers+=1
    if "j" in answerLine:
        num_answers+=1
    if "k" in answerLine:
        num_answers+=1
    if "l" in answerLine:
        num_answers+=1
    if "m" in answerLine:
        num_answers+=1
    if "n" in answerLine:
        num_answers+=1
    if "o" in answerLine:
        num_answers+=1
    if "p" in answerLine:
        num_answers+=1
    if "q" in answerLine:
        num_answers+=1
    if "r" in answerLine:
        num_answers+=1
    if "s" in answerLine:
        num_answers+=1
    if "t" in answerLine:
        num_answers+=1
    if "u" in answerLine:
        num_answers+=1
    if "v" in answerLine:
        num_answers+=1
    if "w" in answerLine:
        num_answers+=1
    if "x" in answerLine:
        num_answers+=1
    if "y" in answerLine:
        num_answers+=1
    if "z" in answerLine:
        num_answers+=1
    return num_answers

#concatenate family answers into one line (familyLine) and store in the list familyAnswers
familyAnswers = []
familyLine = ""
for line in answerList:
    if line == "\n":
        familyAnswers.append(familyLine)
        print(familyLine)
        familyLine = ""
        continue
    if line == answerList[-1]:
        familyLine = familyLine + line
        familyAnswers.append(familyLine)
        print(familyLine)
    line = line.strip()
    line = str(line)
    familyLine = familyLine + line

print(familyAnswers)

count  = 0
for answerLine in familyAnswers:
    line_count = unique_answers(answerLine)
    count = count + line_count

print(count)
