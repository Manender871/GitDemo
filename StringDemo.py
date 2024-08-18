str = "RahulShettyAcademy.com"
str1 = "Consulting firm"
str3 = "RahulShetty"

print(str[1])    # a

print(str[0:5])   # Rahul

print(str + str1)  # Concatenation

print(str3 in str) # Substring validation

var = str.split(".")  # Split String
print(var)  # Print complete split string
print(var[0])  # Print particular section of split string
print(var[1])  # Print particular section of split string

# Trim spaces from left and right side
str4 = " Great "
print(str4.strip())  # Both side trim
print(str4.lstrip())  # Left side trim
print(str4.rstrip()) # Right side trim
