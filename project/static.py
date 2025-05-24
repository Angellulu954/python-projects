class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def getinfo(self):
        return f"{self.name}={self.position}"  
    @staticmethod
    def isvalidposition(position):
        validpositions=["Manger","Cashier","Cook","Janitor"]
        return position in validpositions  
employee1=Employee("Eugene","Manager")
employee2=Employee("Squidward","Cashier")
employee3=Employee("Spongebob","Cook")    
print(Employee.isvalidposition("house keo"))
print(employee1.getinfo())
print(employee2.getinfo())
print(employee3.getinfo())
            