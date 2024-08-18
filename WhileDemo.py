it = 4
while it>1:
    print(it)
    it = it-1
print("while loop execution completed")

print("skip printing 3 in while loop")
it = 4
while it>1:
    if it != 3:
        print(it)
    it = it-1
print("while loop execution completed")

# break statement- to halt loop abruptly.
a = 10
while a>1:
    if a == 3:
        break
    print(a)
    a = a-1
print("while loop execution completed")

# continue statement- to halt current iteration and proceed next iteration.
b = 10
while b>1:
    if b == 9:
        b = b-1
        continue
    if b == 3:
        break
    print(b)
    b = b-1
print("while loop execution completed")
