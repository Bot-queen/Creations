import time
class Pet:
    def introduction(self):
        print("The name of your pet is", self.name)
    def roar(self):
        print(self.sound_type)

class Dog(Pet):
    def bark(self):
        self.sound_type = "woof"
        time.sleep(0.4)
        print(self.sound_type)
    def introduction(self):
        time.sleep(0.4)
        print("Hello, I am", self.name, ". I am a talking dog")

class Cat(Pet):
    def meow(self):
        self.sound_type = "meow"
        time.sleep(0.4)
        print(self.sound_type)
    def introduction2(self):
        time.sleep(0.4)
        print("Hello, I am", self.name, ". I am a talking cat")

choice = input("Choose a pet (cat/dog): ").lower()
if choice == "dog":
    pet1 = Dog()
    time.sleep(0.2)
    name1 = input("Enter your dog's name: ")
    pet1.name = name1
    pet1.introduction()
    pet1.bark()
elif choice == "cat":
    pet2 = Cat()
    name2 = input("Enter your cat's name: ")
    pet2.name = name2
    pet2.introduction2()
    pet2.meow()
else:
    print("Invalid response.")
