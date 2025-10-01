import random
from src.agentClass import Agent
class Food():
    def __init__(self, weight, calories):
        self.weight = random.random() + 1
        self.calories = 1

    def returnTotal(self):
        return self.weight * self.calories

class Milk(Food):
    def __init__(self, weight, calories):
        super().__init__(self, weight, calories)
        self.calories = self.calories * 2

class Sausage(Food):
    def __init__(self, weight, calories):
        super().__init__(self, weight, calories)
        self.weight = self.weight * 2
        self.calories = self.calories * 3

class Cat(Agent):
    def __init__(self):
        super().__init__(self)

    def consume(self, action, food):
        if (action == "Eat" & food == "Sausage"):
            self.performance += Sausage.returnTotal()
        elif (action == "Drink" & food == "Milk"):
            self.performance += Milk.returnTotal()
        else:
            self.performance -= 1