#exception handling in python
#zerodivision error using try-except block
def division(x,y):
    print("this function determines the division of two numbers")
    try:
        result=x/y
        return result
    except ZeroDivisionError:
        print("cannot perform division because denominator cannot be zero")
    finally:
        print("successfully function executed")
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
division_of_numbers=division(num1,num2)
print("the division of two numbes is"+str(division_of_numbers))