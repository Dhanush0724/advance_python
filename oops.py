# class student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def print(self):
#         print("Name :",self.name)
#         print("Age:",self.age)
#         print("Grade:",self.grade)

# if __name__ == "__main__":

#     stu = student("james",20,9)
#     stu.print()

class Rectangel:

    def __init__(self,length,width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)
    
    def __str__(self) :
        return f"Rectangle(length={self.length},width = {self.width})"
    
if __name__ == "__main__":

    r1 = Rectangel(5,3)
    print(r1)

    print(f"Area:{r1.area()}")
    print(f"perimter:{r1.perimeter()}")
    
