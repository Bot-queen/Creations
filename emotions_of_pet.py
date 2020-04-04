class Emotions:
    def __init__(self):
        self.happiness = 0
        self.anger = 0
        self.sadness = - self.happiness

    def happy_event(self):
        self.happiness += 10
        self.sadness -= 10

    def sad_event(self):
        self.happiness -= 10
        self.sadness += 10

    def triggering_event(self):
        self.anger += 10
        self.happiness -= 5
        self.sadness += 5

    def neutralization(self):
        if self.sadness < 0:
            self.sadness = 0
            self.happiness = 100
            print("Your pet is getting slightly cocky.")
        elif self.happiness > 100:
            self.happiness = 100
            self.sadness = 0
            print("Your pet is getting slightly cocky.")
        elif self.happiness < 0:
            self.happiness = 0
            self.sadness = 100
            print("Be nicer!")
        elif self.anger < 0:
            self.anger = 0
        elif self.anger > 100:
            self.anger = 100
        elif self.sadness > 100:
            self.sadness = 100
            self.happiness = 0
            print("Be nicer!")

emotions = Emotions()

def action(pet, name):
    e = 0
    while True:
        try:
            a = str(input("What would you like to do to {}? [A]hug it, [B]hit it, [C]see stats").format(name)).lower()
            if a == "a":
                print("You hugged your", pet)
                emotions.happy_event()
                if emotions.happiness > 40 and emotions.sadness < 15:
                    print("Your {} is happy!").format(pet)
                elif emotions.happiness >= 100 and emotions.sadness == 0:
                    print("Your dog bit you! Maybe its taking you too lightly.")
                else:
                    print("Your dog's face has a slight smile")
            elif a == "b":
                print("You hit", name)
                emotions.sad_event()
                if emotions.sadness > 40 and emotions.happiness < 15:
                    print("Your dog has some tears in its eyes")
                elif emotions.sadness >= 100 and emotions.happiness == 0:
                    print("Your dog is getting suicidal")
                else:
                    print("Your dog has a sad expression...")
            elif a == "c":
                print(name, "has", emotions.happiness, "happiness and", emotions.sadness, "sadness")
            else:
                print("Invalid input")

        except:
            print("Invalid response!")

        e += 1
        if e > 5:
            print("Your {} is starving".format(pet))
            feed = str(input("Feed it? (y/n)"))
            if feed == "y":
                print("You fed your {}".format(pet))
                e = 0
                continue
            elif feed == "n":
                print("Your {} died...".format(pet))
                break
            else:
                print("You didn't do anything, so {} died...".format(name))
                break

n = input("Enter the name for your pet: ")
p = input("Enter the species of the pet: ")
action(p, n)
