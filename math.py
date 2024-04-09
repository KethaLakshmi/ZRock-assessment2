import math
def square_root(n):
    result=math.sqrt(n)
    return  result
while True:
     number=int(input("enter a number:"))
     square=square_root(number)
     print("the square root  of given number is:\n"+str(square))
     next=input("do you want to continue(yes/no)")
     if next=='no':
          print("exiting")
          break