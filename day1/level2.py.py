frequency = 0
frequencies = []
checked = []
found = False
input = open("input.txt", "r").read().splitlines()
while not found:
    for line in input:
        frequency += int(line);
        if frequency in checked:
            print(frequency)
            exit()
        else:
            checked.append(frequency)