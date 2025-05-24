class Student:
    
    count=0
    totalgpa=0
    
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Student.count+=1
        Student.totalgpa+=gpa
    def getinf0(self):
        return f"{self.name} {self.gpa}" 
    @classmethod
    def getcount(cls):
        return f"Total number of students:{cls.count}"
    @classmethod
    def getaverage(cls):
        if cls.count==0:
            return 0
        else:
            return f"Average gpa: {cls.totalgpa / cls.count:.2f}"
student1=Student("Spongebob",3.2)
student2=Student("Patrick",2.0) 
student3=Student("Sandy",4.0)   
print(Student.getcount())   
print(Student.getaverage())   