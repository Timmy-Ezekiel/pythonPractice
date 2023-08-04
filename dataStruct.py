#practicing Common data structure in Python
#Dict
#this provide us the opportunity to have key and value pairs store in a variable
details = {"name": "Timilehin", "Age":25, "GirlFreind": 'Oluwatunmise'}
details["House"] = "Mercy Land"
print(f"{details['House']}")

#topple
#Topple behaves like a list but it is values cannot be mutated
#and also topple is wrappled in a closed bracket

top = (10.00, 15.00)
for cordinates in top:
    print(f"{cordinates}")

#set
#this allow us to create data structure where all elements are unique
#Topple is related to list but all values are just unique

setter = set()
for i in range(20):
    setter.add(i)
print(f"{setter}")

#list
#this is a mutable data structure. It differs from set because
#values are not neccessarily unique just like thte set.

names = [
    "Timmy",
    "Femi",
    "Olakunle"
]
names.append("Jesus")
print(f"{names}")