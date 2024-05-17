class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name)
    def get(self):
        return self.age
    def set(self,age):
        self.age = age
        return self.age

d = Dog("jam",18)
print(d.set(20))

