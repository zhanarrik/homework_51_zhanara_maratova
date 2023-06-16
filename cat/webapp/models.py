import random


class Cat:
    def __init__(self):
        self.name = ""
        self.age = 1
        self.hunger_level = 40
        self.happiness_level = 40

    def to_feed(self):
        if self.hunger_level < 100:
            self.hunger_level += 15
            self.happiness_level += 5
            if self.hunger_level > 100:
                self.happiness_level -= 30
                self.hunger_level = 100

    def to_play(self):
        if self.hunger_level > 0:
            self.happiness_level += 15
            self.hunger_level -= 10
            if self.hunger_level < 0:
                self.hunger_level = 0
            if random.randint(1, 3) == 3:
                self.happiness_level = 0

    def to_sleep(self):
        self.hunger_level -= 5
        self.happiness_level += 5
        if self.hunger_level < 0:
            self.hunger_level = 0
        if self.happiness_level > 100:
            self.happiness_level = 100

    def set_avatar(self):
        if self.happiness_level <= 33:
            return 'sad_cat.png'
        elif self.happiness_level <= 66:
            return 'neutral_cat.png'
        else:
            return 'happy_cat.png'
