input = open("input.txt", "r").read().splitlines()
twoLetters = 0;
threeLetters = 0;

def Count(string):
    checked = {}
    global twoLetters
    global threeLetters
    threeFound = False
    twoFound = False
    for letter in string:
        if letter in checked:
            checked[letter] += 1
        else:
            checked[letter] = 1
    for value in checked.values():
        if(value == 3 and not threeFound):
            threeLetters += 1
            threeFound = True
        if(value == 2 and not twoFound):
            twoLetters += 1
            twoFound = True

for line in input:
    Count(line)

print(twoLetters * threeLetters)

