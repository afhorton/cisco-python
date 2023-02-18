#For the Cisco Python course:
#This program measures the height
#of a flat pyramid (imagine a wall in the shape
#of a pyramid) built from the number of blocks
#input by the user.

blocks = int(input("How many blocks do you want to use?: "))

height = 0
layers = 1
while layers <= blocks:
    height += 1
    blocks -= layers
    layers += 1

print("Your pyramid is", height,"layers high.")
