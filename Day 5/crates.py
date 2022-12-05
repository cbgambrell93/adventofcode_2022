import re
crate_input = open(r"C:\Users\nobod\OneDrive\Documents\Advent of Code\2022\Day 5\input.txt")
initial_lines = []
stack1 = []
stack2 = []
stack3 = []
stack4 = []
stack5 = []
stack6 = []
stack7 = []
stack8 = []
stack9 = []
instructions = []
stacks = []
stack_test = [stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
part_one_result = []


#open file and write to array
for line in crate_input.readlines():
    if (line[0] != '\n'):
        initial_lines.append(line)
    else:
        continue

#how do i split this stupid array out better?
for line in initial_lines:
    if("move" in line):
        instructions.append(line)
    else:
        stacks.append(line)

#letters per stack are at 1 = 1, 5 = 2, 9 = 3
stacks.reverse()
stack_writter = 1

for line in stacks:
    if(line[1].isupper() or line[1] == ""):
        stack1.append(line[1])
    if(line[5].isupper() or line[5] == ""):
        stack2.append(line[5])
    if(line[9].isupper() or line[9] == ""):
        stack3.append(line[9])
    if(line[13].isupper() or line[13] == ""):
        stack4.append(line[13])
    if(line[17].isupper() or line[17] == ""):
        stack5.append(line[17])
    if(line[21].isupper() or line[21] == ""):
        stack6.append(line[21])
    if(line[25].isupper() or line[25] == ""):
        stack7.append(line[25])
    if(line[29].isupper() or line[29] == ""):
        stack8.append(line[29])
    if(line[33].isupper() or line[33] == ""):
        stack9.append(line[33])
#print(stack1)
#print(stack2)
#print(stack3)

#uncomment stack_test and comment proper_stacking line below it for part 1
for line in instructions:
    proper_stacking = []
    move = re.findall("\d{1,2}" ,line)
    #print(move)
    num_to_move = int(move[0])
    while num_to_move > 0:
        #stack_test[int(move[2])-1].append(stack_test[int(move[1])-1].pop())
        proper_stacking.append(stack_test[int(move[1])-1].pop())
        num_to_move-=1
    #comment out below live for part 1
    proper_stacking.reverse()
    #coment out this for loop to part 1
    for x in proper_stacking:
        stack_test[int(move[2])-1].append(x)
for line in stack_test:
    length = len(line)
    if(length > 0):
        part_one_result.append(line[length-1])

print(''.join(part_one_result))
#print(stack_test)
    