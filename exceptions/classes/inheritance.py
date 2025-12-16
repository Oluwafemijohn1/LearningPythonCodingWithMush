class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")


class Mammal(Animal):
    def __init__(self, name, fur_color):
        super().__init__(name)
        self.fur_color = fur_color

    def walk(self):
        print(f"{self.name} with {self.fur_color} fur is walking.")


class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color)
        self.breed = breed

    def bark(self):
        print(f"{self.breed} dog {self.name} is barking.")


class Cat(Mammal):
    def __init__(self, name, fur_color):
        super().__init__(name, fur_color)

    def meow(self):
        print(f"{self.name} is meowing.")


class Fish(Animal):
    def __init__(self, name, scale_color):
        super().__init__(name)
        self.scale_color = scale_color

    def swim(self):
        print(f"{self.scale_color} fish {self.name} is swimming.")


dog = Dog("Buddy", "Brown", "Golden Retriever")
dog.eat()
dog.walk()
dog.bark()


m = Mammal("Leo", "Gray")
print("m isinstance Animal: ", isinstance(m, Animal))  # True
print("m isinstance Mammal: ", isinstance(m, Mammal))  # True
print("m isinstance Dog: ", isinstance(m, Dog))  # False
print("m isinstance object: ", isinstance(m, object))  # False
print("m is Dog: ", m is Dog)  # False
print("m is Mammal: ", m is Mammal)  # True
print("Mammal is subclass of Animal: ", issubclass(Mammal, Animal))  # True
