input = open("input.txt", "r");
frequency = 0
for line in input:
    frequency += int(line);
print(frequency)