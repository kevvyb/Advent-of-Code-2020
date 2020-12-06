import math

f = open("seats.txt")

seats = []
for line in f:
    seats.append(line)

def determine_row(row):
    fORb = 0
    highRow = 127
    lowRow = 0
    while fORb < 7:
        direction = row[fORb]
        #Either the highest row or the bottom row will
        if direction == "F":
            midRow = math.floor((highRow+lowRow)/2)
            highRow = midRow
        if direction == "B":
            midRow = math.ceil((highRow+lowRow)/2)
            lowRow = midRow
        fORb += 1
    return lowRow

def determine_col(row):
    rORl = 7
    highCol = 7
    lowCol = 0
    while rORl < 10:
        direction = row[rORl]
        #Either the highest row or the bottom row will
        if direction == "L":
            midCol = math.floor((highCol+lowCol)/2)
            highCol = midCol
        if direction == "R":
            midCol = math.ceil((highCol+lowCol)/2)
            lowCol = midCol
        rORl += 1
    return lowCol

def my_seat_id(seatIDs):
    seatIDs.sort()
    indexSeat = 0
    while indexSeat < len(seatIDs):
        id1 = seatIDs[indexSeat]
        id2 = seatIDs[indexSeat+1]
        if (id2 - id1) == 2:
            return (id1+1)
        indexSeat+=1

maxProd = 0
maxRow = None
seatIDs = []
for row in seats:
    finalRow = determine_row(row)
    finalCol = determine_col(row)
    rcProd = (finalRow*8)+finalCol
    seatIDs.append(rcProd)

mySeatID = my_seat_id(seatIDs)
print("My Seat ID:", mySeatID)
