f = open("luggage.txt")

luggageRules = []
for line in f:
    luggageRules.append(line)

#create the dict with lead color to sub colors
colorHeir = {}
leadColor = ""
for rule in luggageRules:
    if "contain no other" in rule:
        continue
    words = rule.split()
    adj1 = words[0]
    color1 = words[1]
    leadColor = adj1 + " " + color1
    num_sub_colors = len(words)/4 -1
    i = 0
    subColorList = []
    subColor = ""
    while i < num_sub_colors:
        adj2 = words[5+(4*i)]
        adj2 = str(adj2)
        color2 = words[6+(4*i)]
        color2 = str(color2)
        subColor = adj2+" "+color2
        subColorList.append(subColor)
        adj2 = ""
        color2 = ""
        subColor = ""
        i+=1
    colorHeir[leadColor] = subColorList
    subColorList = []
print(colorHeir)

desiredColor = "shiny gold"

colorHeirLen = len(colorHeir)
#print(colorHeirLen)

#get a colorList of all colors that can hold shiny gold
colorList = []
for color in colorHeir:
    if desiredColor in colorHeir[color]:
        colorList.append(color)


#find the colors is color list
i=0
while i < len(colorList):
    for color in colorHeir:
        newDesiredColor = colorList[i]
        if newDesiredColor in colorHeir[color]:
            colorList.append(color)
    i+=1


#remove duplicate from colorList
finalColorList = []
for color in colorList:
    if color not in finalColorList:
        finalColorList.append(color)

#print(finalColorList)
#print("Number of colors:", len(finalColorList))
