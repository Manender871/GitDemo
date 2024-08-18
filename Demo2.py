# List  is Data type  that allow multiple values and can be differents data type
values = [1,  2, "Rahul", 4, 5]
print(values[0]) # 1
print(values[3]) # 4
print(values[-1]) # 5 (Last index reference)
print(values[1:3]) # [2, 'Rahul']
values.insert(3, "Shetty")
print(values) # [1, 2, 'Rahul', 'Shetty', 4, 5]
values.append("End")
print(values) # [1, 2, 'Rahul', 'Shetty', 4, 5, 'End']
values[2] = "RAHUL" #Updating
print(values) # [1, 2, 'RAHUL', 'Shetty', 4, 5, 'End']
del values[0] # Deleting index
print(values) #[2, 'RAHUL', 'Shetty', 4, 5, 'End']

# Tuple-  Same as List  but immutable where  updation not possible
Val = (1,2, "Rahul", 4, 5)
print(Val[2])
# Val[2] = "RAHUL"
print(Val)

# Dictionary
dic = {"a": 2, 4: "bcd", "c": "Hello World"}
print(dic[4])
print(dic["c"])

# Create dictionaries dynamically on run time and add data.
dict = {}
dict["First Name"] = "Rahul"
dict["Last Name"] = "Shetty"
print(dict)
dict["Gender"] = "Male"
dict["Age"] = 33
print(dict)
print(dict["Gender"])

