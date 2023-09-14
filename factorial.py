
def rec_factorial(num):
   if (num==1):
       return num
   else:
       return num * rec_factorial(num-1)
 
#Enter input
n = int(input("Enter input number : "))
 
if n < 0:
   print("Factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",n,"is",rec_factorial(n))