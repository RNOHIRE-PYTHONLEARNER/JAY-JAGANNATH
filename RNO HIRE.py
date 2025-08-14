n=int(input("ENTER ANY NUMBER"))

def factorial(n):
 if n<=1:
    return 1
 else:
  return n*factorial(n-1)
print(factorial(n),"is the factorial function")

n=int(input("ENTER ANY NUMBER"))
import math
x=math.sqrt(n)
print("square root:",x)
y=math.log(n)
print("Logarithum:",y)
z=math.sin(n)
print("sine:",z)

