import math

f = open("seats.txt")
#f = ["BBFFFBBRRR"]

seats = []
for line in f:
    seats.append(line)

def determine_row(row):
    print(row)
    fORb = 0
    highRow = 127
    lowRow = 0
    while fORb < 7:
        direction = row[fORb]
        print(direction)
        #Either the highest row or the bottom row will
        if direction == "F":
            midRow = math.floor((highRow+lowRow)/2)
            highRow = midRow
        if direction == "B":
            midRow = math.ceil((highRow+lowRow)/2)
            lowRow = midRow
        fORb += 1
        print("Low Row:",lowRow,"High Row:",highRow)
    print(lowRow)
    return lowRow

def determine_col(row):
    print("Determine column")
    rORl = 7
    highCol = 7
    lowCol = 0
    while rORl < 10:
        direction = row[rORl]
        print(direction)
        #Either the highest row or the bottom row will
        if direction == "L":
            midCol = math.floor((highCol+lowCol)/2)
            highCol = midCol
        if direction == "R":
            midCol = math.ceil((highCol+lowCol)/2)
            lowCol = midCol
        rORl += 1
        print("Low Col:",lowCol,"High Col:",highCol)
    print(lowCol)
    return lowCol

maxProd = 0
maxRow = None
for row in seats:
    finalRow = determine_row(row)
    finalCol = determine_col(row)
    rcProd = (finalRow*8)+finalCol
    print("Product of row and col:",rcProd)
    if rcProd > maxProd:
        print("Highest Row so far:",finalRow,"Highest Col so far:",finalCol)
        maxRow = row
        maxProd = rcProd
print(maxRow)
print("Maximum Seat ID:", maxProd)
