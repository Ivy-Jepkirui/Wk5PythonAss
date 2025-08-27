# Base class
class Pet:
    def __init__(self, name, age, species):
        self.__name = name       # Private attribute
        self.__age = age         # Private attribute
        self.species = species   # Public attribute

    # Encapsulation: Getters and Setters
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

    # Default move method (can be overridden)
    def move(self):
        print("Movement behavior is not defined for this pet.")

    # Default speak method (can be overridden)
    def speak(self):
        print("This pet makes a sound.")

    # Describe method
    def describe(self):
        return f"{self.get_name()} is a {self.get_age()} year old {self.species}."


# Subclass: Dog
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Dog")
        self.breed = breed

    def move(self):
        print("The dog runs on the grass.")

    def speak(self):
        print("The dog says: Woof!")


# Subclass: Cat
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Cat")
        self.color = color

    def move(self):
        print("The cat jumps from furniture to furniture.")

    def speak(self):
        print("The cat says: Meow!")


# Subclass: Bird
class Bird(Pet):
    def __init__(self, name, age, wing_span):
        super().__init__(name, age, "Bird")
        self.wing_span = wing_span

    def move(self):
        print(" The bird flies through the air.")

    def speak(self):
        print(" The bird says: Tweet!")


# Subclass: Fish
class Fish(Pet):
    def __init__(self, name, age, water_type):
        super().__init__(name, age, "Fish")
        self.water_type = water_type  # e.g., Freshwater or Saltwater

    def move(self):
        print("The fish swims in the tank.")

    def speak(self):
        print(" The fish says: Blub blub!")


# Function to demonstrate polymorphism
def show_pet_actions(pet):
    print(pet.describe())
    pet.move()
    pet.speak()
    print("-" * 40)


# Create instances
dog = Dog("Buddy", 3, "Labrador")
cat = Cat("Whiskers", 2, "Tabby")
bird = Bird("Chirpy", 1, "15 cm")
fish = Fish("Bubbles", 1, "Freshwater")

# Demonstrate polymorphic behavior
show_pet_actions(dog)
show_pet_actions(cat)
show_pet_actions(bird)
show_pet_actions(fish)
