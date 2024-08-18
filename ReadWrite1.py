# Read all text line by line using readline() cmd.
file = open('Test.txt')

line = file.readline()
while line != "":
    print(line)
    line = file.readline()

file.close()

