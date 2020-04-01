import time
class Pet:
  def __init__(self):
    self.name = ""
    self.age = ""
    self.height = ""
    self.sound = ""
    self.species = ""
    
  def roar(self):
    time.sleep(0.4)
    print(self.sound, "!")
  
  def introductions(self):
    time.sleep(0.4)
    print("Your {}'s name is ".format(self.species), self.name)

class Dog(Pet):
  def intro(self):
    self.species = "dog"
    Pet().introductions()
  
  def bark(self):
    self.sound = "woof"
    Pet().roar()
    
class Cat(Pet):
  def intro(self):
    self.species = "cat"
    Pet().introductions()
  
  def cat_sound(self):
    self.sound = "meow"
    Pet().roar()
    
if __name__ == "__main__":
  time.sleep(0.2)
  n = input("Enter pet's name: ")
  time.sleep(0.2)
  a = int(input("Enter pet's age: "))
  time.sleep(0.2)
  h = float(input("Enter pet's height: "))
  time.sleep(0.2)
  s = input("Enter pet's species (cat/dog): ").lower()
  if s == "dog":
    pet = Dog()
    pet.name = n 
    pet.age = a
    pet.height = h
    pet.introductions()
    pet.bark()
  elif s == "cat":
    pet = Cat()
    pet.name = n 
    pet.age = a
    pet.height = h
    pet.introductions()
    pet.cat_sound()
  elif s != "dog" or s != "cat":
    print("Pet species unknown...")
