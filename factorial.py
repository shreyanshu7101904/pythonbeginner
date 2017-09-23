
# Python program to find the factorial 
val = int(input("Enter a number: "))

fac = 1

# check if the number is negative, positive or zero
if val < 0:
   print("factorials for negative number is invalid")
elif val == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,val + 1):
       fac = fac*i
   print("The factorial of",val,"is",fac)
