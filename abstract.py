from abc import ABC,abstractmethod

class shape(ABC):        #here ABC is a meta class
    @abstractmethod
    def print_area(self):
        return 0

    def water(self):
        return f"hello kumar"

class Rectangle(shape):
    sides=4
    type="Rectangle"

    def __init__(self):
        self.length=6
        self.breath=7

    def print_area(self):
        return self.length*self.breath

    def gaurav(self):
        return "sujit"

rect1=Rectangle()
print(rect1.print_area())
print(rect1.gaurav())
print(rect1.water())