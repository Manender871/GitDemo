file = open('Test.txt')
# read all contents of file
#print(file.read())
# read n numbers of characters by passing parameters
#print(file.read(5))

# read  one single line at a time using readline()
print(file.readline())  # read first line
print(file.readline())  # read second line
file.close()
