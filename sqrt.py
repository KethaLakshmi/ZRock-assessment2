#python function that returns  square of a number
def square_root( n):
     square=n*n
     return square
while True:
     number=int(input("enter a number:"))
     result=square_root(number)
     print("the square of given number is:\n"+str(result))
     next=input("do you want to continue(yes/no)")
     if next=='no':
          print("exiting")
          break
