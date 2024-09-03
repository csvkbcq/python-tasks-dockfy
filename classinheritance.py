class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "Some sound"
class Dog(Animal):
    def speak(self):
        return "Woof!"
my_dog = Dog("Buddy")
print(my_dog.name) 
print(my_dog.speak())
