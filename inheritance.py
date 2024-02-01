class Circle:
    def __init__(self,radius):  
        self.radius = radius

    def find_area(self):
        return 3.14*self.radius**2


my_circle = Circle(5)
print(my_circle.find_area())






class Animal:
    def __init__(self,name):
        self.name= name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says meow"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says woof"
    
dog = Dog("lala")
cat = Cat("haha")

print(dog.speak())
print(cat.speak())