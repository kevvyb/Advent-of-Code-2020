file_import = open("passports.txt")

##file_import = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm",""]

pports = []
for line in file_import:
    pports.append(line)

#four digits after byr between 1920 and 2002
def _check_byr(pport):
    byrIndex = pport.index("byr")
    num = pport[(byrIndex+4):(byrIndex+8)]
    num = int(num)
    if num >= 1920 and num <= 2002:
        return True
    else:
        return False

#four digits after iyr between 2010 and 2020
def _check_iyr(pport):
    iyrIndex = pport.index("iyr")
    num = pport[(iyrIndex+4):(iyrIndex+8)]
    num = int(num)
    if num >= 2010 and num <= 2020:
        return True
    else:
        return False

#four digits after eyr between 2020 and 2030
def _check_eyr(pport):
    eyrIndex = pport.index("eyr")
    num = pport[(eyrIndex+4):(eyrIndex+8)]
    num = int(num)
    if num >= 2020 and num <= 2030:
        return True
    else:
        return False

#number followed by cm or in. If cm, number between 150 and 193. If in, number between 59 and 76
def _check_hgt(pport):
    lng = len(pport)
    hgtIndex = pport.index("hgt")
    pportHgt = pport[hgtIndex:(hgtIndex+10)]
    if "cm" in pportHgt:
        cmIndex = pportHgt.index("cm")+hgtIndex
        height = pport[(hgtIndex + 4): cmIndex]
        height = int(height)
        if height >= 150 and height <= 193:
            return True
        else:
            return False
    if "in" in pportHgt:
        inIndex = pportHgt.index("in")+hgtIndex
        height = pport[(hgtIndex + 4): inIndex]
        height = int(height)
        if height >= 59 and height <= 76:
            return True
        else:
            return False
    else:
        return False

# a '#' followed by exactly six characters
def _check_hcl(pport):
    hclIndex = pport.index("hcl")
    lng = len(pport)
    if pport[hclIndex+4] == "#":
        charList = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        char1 = pport[hclIndex+5]
        char2 = pport[hclIndex +6]
        char3 = pport[hclIndex +7]
        char4 = pport[hclIndex +8]
        char5 = pport[hclIndex +9]
        char6 = pport[hclIndex +10]
        char7 = pport[hclIndex + 11]
        hclList = [char1,char2,char3,char4,char5,char6]
        check = all(item in charList for item in hclList)
        #handling if hcl item is at the end of the line
        if (hclIndex+12) == lng:
            if check is True:
                return True
            else:
                return False
        if char7 != None and char7 != " ":
            return False

        if check is True:
            return True
        else:
            return False
    else:
        return False

#exactly one of the colors in the colorList below
def _check_ecl(pport):
    lng = len(pport)
    eclIndex = pport.index("ecl")
    colorList = ["amb","blu","brn","gry","grn","hzl","oth"]
    #if ecl item is at the end of the line
    if lng == eclIndex + 8:
        eyeCol = pport[(eclIndex+4):(eclIndex+7)]
        if eyeCol in colorList:
            return True
        else:
            return False
    try:
        spaceIndex = pport.index(" ", eclIndex)
        eyeCol = pport[(eclIndex+4):spaceIndex]
    except:
        eyeCol = pport
        eyeCol = pport[(eclIndex+4):(eclIndex+8)]

    if eyeCol in colorList:
        return True
    else:
        return False

#a nine-digit number, including leading zeroes
def _check_pid(pport):
    pport = pport.strip()
    lng = len(pport)
    pidIndex = pport.index("pid")
    #This if statement handles if pid is at the end of the line
    if (pidIndex + 13) == lng:
        num = pport[(pidIndex+4):(pidIndex+13)]
        try:
            num = int(num)
            return True
        except:
            return

    #if the 10th character after pid: is not a blank, return False
    try:
        tenthChar = pport[pidIndex+13]
        if tenthChar != "" and tenthChar != " " and tenthChar != None:
            return False
    except IndexError:
        num = pport[(pidIndex+4):(pidIndex+13)]

    num = pport[(pidIndex+4):(pidIndex+13)]
    try:
        num = int(num)
        return True
    except:
        return False

def _check_for_fields(pport):
    reqs = 0
    print(pport)
    if "byr" in pport:
        if _check_byr(pport):
            print("byr GOOD")
            reqs += 1
    if "iyr" in pport:
        if _check_iyr(pport):
            print("iyr GOOD")
            reqs += 1
    if "eyr" in pport:
        if _check_eyr(pport):
            print("eyr GOOD")
            reqs += 1
    if "hgt" in pport:
        if _check_hgt(pport):
            print("hgt GOOD")
            reqs += 1
    if "hcl" in pport:
        if _check_hcl(pport):
            print("hcl GOOD")
            reqs += 1
    if "ecl" in pport:
        if _check_ecl(pport):
            print("ecl GOOD")
            reqs += 1
    if "pid" in pport:
        if _check_pid(pport):
            print("pid GOOD")
            reqs += 1
    return reqs



num_lines = len(pports)

line_num = 0
num_req_fields = 0
valid_count = 0

for pport in pports:
    line_num +=1
    num_req_fields  = num_req_fields + _check_for_fields(pport)
    if not pport.strip() or line_num == num_lines:
        if num_req_fields == 7:
            valid_count += 1
            print("Valid:",valid_count)
        num_req_fields = 0
        continue

print("Number of valid passports:", valid_count)
