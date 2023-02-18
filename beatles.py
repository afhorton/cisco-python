#For the Cisco Python course:
#This program adds elements to the list "beatles"
#printing off the band's varying roster
#and its final number of members.

beatles = []

og_members = ['John Lennon', 'Paul McCartney', 'George Harrison']

add_members = ['Stu Sutcliffe', 'Pete Best']

# Don't use 'beatles += mem'.  It will add names as separate letters to list 
for mem in og_members:
    beatles.append(mem)

for mem in add_members:
    beatles.append(mem)

print(beatles)

del beatles[-1]
del beatles[-1]

print(beatles)

beatles.insert(-1, 'Ringo Starr')

print(beatles)
print("There are " + str(len(beatles)) + " Beatles.")
