Input = open("input.txt", "r").read().splitlines()
Input.sort()
CurentGuard = ""
WakeUp = 0
Fallen = 0
Guards = []
Sleep = {}
SleepHours = {}
# 3041 sleeps 542 hours

def FindMax(array):
    Max = 0    
    Id = 0
    for key,value in array.items():
        if(value > Max):
            Max = value
            Id = key
    return str(Max) + " : " + str(Id)

for i in range(len(Input)):
    _Input = Input[i].replace("[", "").replace("]", "").split()
    Data = _Input[0]
    Command = _Input[2]
    if(Command == "Guard"):
        CurentGuard = _Input[3]
        if CurentGuard not in Guards:
            Guards.append(CurentGuard)
            Sleep[CurentGuard] = 0
    if(Command == "falls"):
        Fallen = int(_Input[1].split(":")[1])
    if(Command == "wakes"):
        WakeUp = int(_Input[1].split(":")[1])
        Sleep[CurentGuard] += int(WakeUp) - int(Fallen)
        if(CurentGuard == "#3041"):
            for Minute in range(Fallen, WakeUp):
                if Minute not in SleepHours:
                    SleepHours[Minute] = 0
                else:
                    SleepHours[Minute] += 1

GuardId = int(FindMax(Sleep).replace("#", "").split()[2])
Minute = int(FindMax(SleepHours).split()[2])
print(GuardId * Minute)