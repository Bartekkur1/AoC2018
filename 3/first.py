Map = [[0 for x in range(1000)] for y in range(1000)] 
input = open("input.txt", "r").read().splitlines()
count = 0

def FillMap(posX, posY, lenX, lenY):
    for y in range(posY, posY + lenY):
        for x in range(posX, posX + lenX):
            Map[x][y] += 1

for line in input:
    lenX = line.split()[3].split("x")[0]
    lenY = line.split()[3].split("x")[1]
    posX = line.split()[2].split(",")[0]
    posY = line.split()[2].split(",")[1].replace(":", "")
    FillMap(int(posX), int(posY), int(lenX), int(lenY))

for line in Map:
    for num in line:
        if num >= 2:
            count += 1

print(count)