class Emotions:
    def __init__(self):
        self.happiness = 0
        self.anger = 0
        self.sadness = - self.happiness
    def happy_event(self):
        self.happiness += 10
        self.sadness -= 10

    def triggering_event(self):
        self.anger += 10
        self.happiness -= 5
        self.sadness += 5

    def neutralization(self):
        if self.sadness < 0:
            self.sadness = 0
            self.happiness = 100
        elif self.happiness > 100:
            self.happiness = 100
            self.sadness = 0
        elif self.happiness < 0:
            self.happiness = 0
            self.sadness = 100
        elif self.anger < 0:
            self.anger = 0
        elif self.anger > 100:
            self.anger = 100
        elif self.sadness > 100:
            self.sadness = 100
