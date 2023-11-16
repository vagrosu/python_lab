class Animal:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print("I am eating")


class Mammal(Animal):
    def __init__(self, name, age, color, legs, is_herbivorous):
        super().__init__(name, age, color)
        self.legs = legs
        self.is_herbivorous = is_herbivorous

    def eat(self):
        if self.is_herbivorous:
            print("I am eating grass")
        else:
            print("I am eating meat")


class Bird(Animal):
    def __init__(self, name, age, color, is_nocturne):
        super().__init__(name, age, color)
        self.is_nocturne = is_nocturne

    def eat(self):
        print("I am eating seeds")


class Fish(Animal):
    def __init__(self, name, age, color, weight):
        super().__init__(name, age, color)
        self.weight = weight

    def eat(self):
        print("I am eating plankton")


if __name__ == '__main__':
    mammal = Mammal("Dog", 6, "brown", 4, False)
    print(mammal.name)
    print(mammal.age)
    print(mammal.color)
    print(mammal.legs)
    mammal.eat()

    print()
    bird = Bird("Flamingo", 5, "pink", False)
    print(bird.name)
    print(bird.age)
    print(bird.color)
    print(bird.is_nocturne)
    bird.eat()

    print()
    fish = Fish("Catfish", 1, "grey", 4)
    print(fish.name)
    print(fish.age)
    print(fish.color)
    print(fish.weight)
    fish.eat()
