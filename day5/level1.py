File = open("input.txt", "r").read()
Input = []
Output = ""

for i in range(len(File)):
    Input.append(File[i])

i = 0
while i < len(Input) - 1:
    if Input[i].upper() == Input[i + 1].upper() and Input[i] != Input[i + 1]:
        del Input[i]        
        del Input[i]
        i = max(0, i - 1)
    else:
        i += 1

print(''.join(Input))
print(len(Input))