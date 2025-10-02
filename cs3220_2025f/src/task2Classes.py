import random
from src.agentClass import Agent
from src.agentPrograms import TableDrivenAgentProgram
class Food():
    def __init__(self, weight, calories):
        self.weight = random.random() + 1
        self.calories = 1

    def returnTotal(self):
        return self.weight * self.calories

class Milk(Food):
    def __init__(self, weight, calories):
        super().__init__(weight, calories)
        self.calories = self.calories * 2

class Sausage(Food):
    def __init__(self, weight, calories):
        super().__init__(weight, calories)
        self.weight = self.weight * 2
        self.calories = self.calories * 3

class Cat(Agent):
    def __init__(self, table):
        self.alive = True
        self.program = TableDrivenAgentProgram(table=table)
        self.performance = 2

    def consume(self, food):
        if (food == "Sausage"):
            food = Sausage(1, 1)
            self.performance += food.returnTotal()
        elif (food == "Milk"):
            food = Milk(1, 1)
            self.performance += food.returnTotal()
        else:
            self.performance -= 1

    def is_alive(self):
        return self.alive
