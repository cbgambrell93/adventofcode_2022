camp_clean = open(r"C:\Users\nobod\OneDrive\Documents\Advent of Code\2022\Day 4\input.txt")
assignments = []
cleaningCount = 0
duplicateSections = 0

#open file and write to array
for line in camp_clean.readlines():
    if (line[0] != '\n'):
        assignments.append(line)
    else:
        continue

result = []
#split out into number variables
for assign in assignments:
    listone = []
    listtwo = []
    elfcounter = 1
    for part in assign.split(","):
        #write to first elf list
        if(elfcounter == 1):
            if('-' in part):
                a, b = part.split('-')
                a, b = int(a),int(b)
                listone.extend(range(a, b+1))
            else:
                a = int(part)
                listone.append(a)
        #write to second elf list
        if(elfcounter == 2):
                if('-' in part):
            #write to first elf list
                    a, b = part.split('-')
                    a, b = int(a),int(b)
                    listtwo.extend(range(a, b+1))
                else:
                    a = int(part)
                    listtwo.append(a)
        elfcounter+=1

    elfone = set(listone)
    elftwo = set(listtwo)
    if(elfone.issubset(elftwo) or elftwo.issubset(elfone)):
        cleaningCount+=1
    #if(any(i in elfone for i in elftwo) or any(i in elfone for i in elftwo)):
    if(elfone.intersection(elftwo)): 
        duplicateSections+=1
print("Part One Answer")
print(cleaningCount)

#PART TWO
print("Part Two Answer")
print(duplicateSections)   
   
