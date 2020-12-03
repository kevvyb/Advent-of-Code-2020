forest = open("trees.txt")
flist = []
for forestrows in forest:
    flist.append(forestrows)

#y = row, where top row is 1
#x = index in line



#forest = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]

runs = [1,3,5,7,1]
rises = [1,1,1,1,2]
treeList = []

slopecnt = 0
for run in runs:
    print("Run:", run)

    rise = rises[slopecnt]
    print("Rise:", rise)
    #we have the x move and y move (run, rise)
    rownum = 0
    colnum = 0
    treeCnt = 0
    for row in flist:
            print(rownum, rise)
            #only assess line if it is a multiple of the rise
            if rownum % rise != 0:
                rownum = rownum + 1
                continue
            #print and strip empty spaces
            print(row)
            row = row.strip()
            #get length
            lng = len(row)

            loc = colnum % lng
            char = row[loc]
            if char == "#":
                treeCnt = treeCnt + 1
                print("HIT")
            colnum = colnum + run
            rownum = rownum + 1

    treeList.append(treeCnt)
    slopecnt = slopecnt + 1



print(treeList)
product = 1
for treect in treeList:
    product = treect*product

print(product)
