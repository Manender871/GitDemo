print('Hello')
# Hello

a = 3
print(a)

Str = "Hello World"
print(Str)

b, c, d = 5,  6.4,  "Great"
print(b)
print(c)
print(d)
#print ("value is"+a) Error as can only concatenate str(not "int") to str

print("{} {}".format("Value is",b))
print(type(b))
print(type(c))
print(type(d))
a = 100
print("Value",a,"is",type(a))
b = 10.25
print("Value",b,"is",type(b))
c = 10+3j
print("Value",c,"is",type(c))
a = "String in a double quote"
b = 'String  in a single  quote'
print(a)
print(b)
# Concatenate with,
print(a,"concatenate with",b)
# Concatenate with +
print(a + " concatenate with " + b)