class Student:
    year=2028
    numstudents=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.numstudents+=1
student1=Student("Spongebob",30)
student2=Student("Patrick",35)
student3=Student("Squidward",53)
student4=Student("Sandy",25) 

print(Student.numstudents)    
print(f"My graduating class of {Student.year} has {Student.numstudents} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)