# print all text line by line using readlines() cmd .
# readlines() create list.

file = open('Test.txt')

for line in file.readlines():  # create all line text as list
    print(line)

file.close()
