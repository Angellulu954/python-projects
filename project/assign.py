# Functions to Handles calculations
import math
print("//Simple calculator//")
def add(a,b):
    
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "You cannot divide a number by zero"
    except ArithmeticError:
        return "Arithmetic error"
def squareroot(a):
        if a>=0:
            return math.sqrt(a)
        else:
            return "You cannot calculate the square root of a negative number"
def power(x,y) :
    return x**y             
            
def percentage(x,y):
    return (x/100)*y            


memory=0
while True:
    # User inputs
    # Choosing the operation they need 
    print("\n 1.Addition\n2.Subtraction\n 3.Division\n4.Multiplication\n5.Exit.\n6.Percentage calculation\n7.squareroot\n8.power calculation")
    print("Memory options. \n9.Add to memory\n10.Clear Memory.")
    option=input("Enter a value between 1 and 10:")
    if not option.isdigit() or option not in ["1", "2", "3", "4", "5","6","7","8","9","10"]:
        print("Invalid option. Please enter a number between 1 and 10.")
        continue
    if option=="5":
        print("Exiting....")
        break
    if option=="9":
        if 'result' in locals():
            memory=result
            print("Memory updated.")
        else:
            print("No value to add to memory")  
        continue    
    if option=="10":
        if memory==0:
            print("Memory is already cleared")
        else:
            memory=0
            print("Memory Cleared") 
        continue         
    # To handle entry of non numbers gracefully
    print("Enter (mr) if you want to use a value from memory ")
    try:
        if option=="7":
            x=input("Enter the value:")
            if x.strip().lower()=="mr":
                x=memory
            else:
                x=float(x)    
        else:    
            x=input("Enter the first value:")
            if x.strip().lower()=="mr":
                x=memory
            else:
                x=float(x)    
            y=input("Enter the second value:")
            if y.strip().lower()=="mr":
                y=memory
            else:
                y=float(y)   
    except ValueError:
        print("Please enter a number") 
        # skips over the rest of the loop and starts from the top
        continue   
    if option=="1":
        result=add(x,y)
        print(f"Result:{x} + {y}= {result}")
    elif option=="2":
        result=subtract(x,y)
        print(f"Result:{x} - {y}= {result}")
    elif option=="3":
        result=divide(x,y)
        print(f"Result:{x} / {y}= {result}")
    elif option=="4":
        result=multiply(x,y) 
        print(f"Result:{x} * {y} = {result}")
    elif option=="6":
        result=percentage(x,y)
        print(f"Result:({x}/100) * {y}= {result}")
    elif option=="7" :
        result=squareroot(x)
        print(f"Result: sqrt{x} = {result}")   
    elif option=="8":
        result=power(x,y)
        print(f"Result:{x} ^ {y}= {result}")      

    