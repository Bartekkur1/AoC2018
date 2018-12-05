Kek = open("input.txt", "r").read()
Output = []

def React(string):
    Input = []
    for i in range(len(string)):
        Input.append(string[i])
    i = 0
    while i < len(Input) - 1:
        if Input[i].upper() == Input[i + 1].upper() and Input[i] != Input[i + 1]:
            del Input[i]        
            del Input[i]
            i = max(0, i - 1)
        else:
            i += 1
    return Input

for i in range(ord('a'), ord('z')):
    TestCase = Kek
    TestCase = TestCase.replace(chr(i), "")
    TestCase = TestCase.replace(chr(i).upper(), "")
    Output.append(len(React(TestCase)))

Output.sort()
print(Output)
