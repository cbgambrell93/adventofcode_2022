com_file = open(r"C:\Users\nobod\OneDrive\Documents\Advent of Code\2022\Day 6\input.txt")
com_signal = com_file.readline()

com_length = len(com_signal)
com_read_place = 0
com_initial = []
com_array = []
com_end = []

while com_read_place < 4:
    com_initial.append(com_signal[com_read_place])
    com_array.append(com_signal[com_read_place])
    com_read_place+=1

#while com_read_place < com_length:
while len(com_initial) != len(set(com_initial)):
    com_initial.pop(0)
    com_initial.append(com_signal[com_read_place])
    com_array.append(com_signal[com_read_place])
    com_read_place+=1

print("Size before begininning marker")
print(len(com_array))

#Part 2
#Lets reset our storage
com_read_place = 0
com_initial = []
com_array = []
com_end = []
while com_read_place < 14:
    com_initial.append(com_signal[com_read_place])
    com_array.append(com_signal[com_read_place])
    com_read_place+=1

#while com_read_place < com_length:
while len(com_initial) != len(set(com_initial)):
    com_initial.pop(0)
    com_initial.append(com_signal[com_read_place])
    com_array.append(com_signal[com_read_place])
    com_read_place+=1

print("Size before Message marker")
print(len(com_array))