forest = open("trees.txt")

#y = row, where top row is 1
#x = index in line

treeCnt = 0

#forest = ["..##.......","#...#...#..",".#....#..#.","..#.#...#.#",".#...##..#.","..#.##.....",".#.#.#....#",".#........#","#.##...#...","#...##....#",".#..#...#.#"]
x=0
y=1
#
#THIS DID NOT WORK. The lengths are all the same so I just wanted to get it once. But in the second for loop run (line 20), the second line in the file was pulled on the first iteration.
#for row in forest:
#    lng = len(row)
#    break

#move to the next row, check if location has a tree, add to tree count if so\
ycount = 0

for row in forest:
        print(row)
        row = row.strip()
        lng = len(row)
        loc = x % lng
        char = row[loc]
        if char == "#":
            treeCnt = treeCnt + 1
            print("HIT")
        x = x + 3
        y=y+1



print("Trees hit:", treeCnt)
