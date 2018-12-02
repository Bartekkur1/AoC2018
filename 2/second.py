found = []
names = open("input.txt", "r").read().splitlines()
searching = True

def OneDiff(string1, string2):
    diff = 0;
    for i in range(len(string1)):
        if(string1[i] != string2[i]):
            diff += 1
    if(diff == 1):
        StringDiff(string1, string2)

def StringDiff(string1, string2):
    global searching
    if(len(string1) == len(string2) and searching):
        for i in range(len(string1)):
            if(string1[i] == string2[i]):
                found.append(string1[i])
                searching = False

for line1 in names:
    for line2 in names:
        OneDiff(line1, line2)

print(''.join(found))