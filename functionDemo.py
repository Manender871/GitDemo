# In Python funtion is a group of related statements that perform a specific taks.

def greetme():
    # function declaration
    print("Good Morning")


# function call
greetme()


def greetme(name):
    print("Good Morning:"+name)


# Sum of two integer using func
def addinteger(a, b):
    print("Sum of two integer:",a+b)


greetme("Rahul Sheety")
addinteger(2,3)


def diffinteger(a, b):
    return a-b


print("Different of two integer:",diffinteger(10,4))

