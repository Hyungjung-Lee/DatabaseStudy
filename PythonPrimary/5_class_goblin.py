class Goblin:
    def __init__(self, name, position, life, power):
        self.name = name
        self.position = position
        self.power = power
        self.life = life

    def print1(self):
        print(f"{self.name} position {self.position} power {self.power} life {self.life}")

    def damage(self, power):
        self.life -= 10
        if self.life < 0:
            print(f"{self.name} dead ")