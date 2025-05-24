class Animal:
    def __init__(self,name):
        self.name=name
        self.isalive=True
    def eat(self):
        print(f"{self.name} is eating ")
    def sleep(self):
        print(f"{self.name} is asleep")  
class Dog(Animal):
    def speak(self):
        print("WOOF!")         
class Cat(Animal):
    def speak(self):
        print("MEOW!")
class Mouse(Animal):
    def speak(self):
        print("SQURRCK!")
dog=Dog("Scobby")
cat=Cat("Garfield")
mouse=Mouse("Jerry")
print(dog.name)
print(dog.isalive)

dog.eat()
dog.sleep()
mouse.speak()
    