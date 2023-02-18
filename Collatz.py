#For the Cisco Python course:
#This program puts a number through Collatz' formulas to see
#if it adheres to his conjecture.
#It also prints the number steps it took
#to wittle a number down to 1.


c0 = int(input("Throw me a number: "))

if c0 > 1:
  steps = 0
  while c0 != 1:
    if c0 % 2 != 0:
      cnew = 3 * c0 + 1
    else:
      cnew = c0 // 2
    print(c0)
    c0 = cnew
    steps += 1
    print("steps =", steps)
else:
  print("Not a good c0 number.")
