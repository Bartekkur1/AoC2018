Map = [[0 for x in range(1000)] for y in range(1000)] 
Overlap = {}
input = open("input.txt", "r").read().splitlines()

for x in range(1000):
    for y in range(1000):
        Map[x][y] = []

def FillMap(Id, posX, posY, lenX, lenY):
    for y in range(posY, posY + lenY):
        for x in range(posX, posX + lenX):
            if(len(Map[x][y]) > 0):
                Overlap[Id] = True
                for MapId in Map[x][y]:
                    Overlap[MapId] = True
            elif(Id not in Overlap):
                Overlap[Id] = False
            Map[x][y].append(Id)

for line in input:
    Id = line.split()[0]
    lenX = line.split()[3].split("x")[0]
    lenY = line.split()[3].split("x")[1]
    posX = line.split()[2].split(",")[0]
    posY = line.split()[2].split(",")[1].replace(":", "")
    FillMap(Id, int(posX), int(posY), int(lenX), int(lenY))

for key,value in Overlap.items():
    if not value:
        print(key + "" + str(value))