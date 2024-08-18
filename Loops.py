
greeting = "Good Morning"
if greeting == "Good Morning":
    print("Condition Matched")
    print(greeting)
else:
    print("Condition don't matched")
print("if-else condition  code  completed")

a = 4
if a > 2:
    print("Condition matched")
    print("a is greater than 2")
else:
    print("Condition don't match")
print("if-else condition code completed")

#  for Loop
# Iterate all values in List
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i)
# Print the list with multiple by 2
obj = [2, 3, 5, 7, 9]
for i in obj:
    print(i*2)

# Sum of first 5 natural number
# range(i, j)-> i to j-1
summation = 0
for j in range(1,6):
    summation = summation + j
print("Sum of first 5 natural number=",summation)

print("XXXXXXXXXXXXrange funct with skipping valueXXXXXXXXXX")
for k in range(1, 10, 2):
    print(k)
for n in range(1, 10, 5):
    print(n)

print("range func if skipping first index treated first index as 0")
for m in range(5):
    print(m)




