# read the file and store all the lines in list.
# reverse the list
# write the list back to the file.

with open('Test.txt', 'r') as reader:
    content = reader.readlines()  # [app, ball, cat, dog, elephant]
    reversed(content)
    with open('Test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)


