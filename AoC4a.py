file_import = open("passports.txt")

##file_import = ["ecl:gry pid:860033327 eyr:2020 hcl:#fffffd", "byr:1937 iyr:2017 cid:147 hgt:183cm",""]

pports = []
for line in file_import:
    pports.append(line)

def _check_for_fields(pport):
    reqs = 0
    print(pport)
    if "byr" in pport:
        reqs += 1
    if "iyr" in pport:
        reqs += 1
    if "eyr" in pport:
        reqs += 1
    if "hgt" in pport:
        reqs += 1
    if "hcl" in pport:
        reqs += 1
    if "ecl" in pport:
        reqs += 1
    if "pid" in pport:
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
