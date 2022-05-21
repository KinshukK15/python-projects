parrot = "Norwegian Blue"

print(parrot)

print(parrot[3]) #indexing

print(parrot[-7]) #negative indexing

print()
#Slicing

parrot = "Norwegian Blue"

print(parrot[0:6]) #Norweg
print(parrot[3:5])
print(parrot[0:9])#or
print(parrot[:9])

print()

print(parrot[10:14]) #or
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

print()
print()
print()
 # Negative slicing

print(parrot[-4:-2]) #Bl
print(parrot[-4:12]) #Bl

print()
# slicing in a step

print(parrot[0:6:2]) #Nre
print(parrot[0:6:3]) #Nw

number = "9,223;372:036 854,775;807"
seperators= number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val)for val in values])

