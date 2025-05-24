def addsprinkles(func):
    def wrapper(*args,**kwargs):
        print("** You add sprinkles🍡 **")
        func(*args,**kwargs)
    return wrapper
def addfudge(func):
    def wrapper(*args,**kwargs):
        print("** You add fudge 🍫 **") 
        func(*args,**kwargs)
    return wrapper 
@addsprinkles   
@addfudge 
def geticecream(flavour):
    print(f"Here is your {flavour} ice cream 🍧")
geticecream("strawberry")
    
    