from src.environmentClass import Environment
from src.locations import *
from src.task2Classes import *
import random

class CatFriendlyHouseEnvironment(Environment):
    def __init__(self):
        super().__init__()
        self.status = {loc_A: random.choice(['Milk', 'Sausage']),
                       loc_B: random.choice(['Milk', 'Sausage'])}
        
    def percept(self, agent):
        return agent.location, self.status[agent.location]
    
    def is_agent_alive(self, agent):
        return agent.alive
    
    def update_agent_alive(self, agent):
        if (agent.performance <= 0):
            agent.alive = False
            print("Agent {} is dead".format(agent))

    def execute_action(self, agent, action):
        if (self.is_agent_alive(agent)):
            if action == "Left":
                agent.location = loc_A
                agent.performance -= 1
                self.update_agent_alive(agent)
            elif action == "Right":
                agent.location = loc_B
                agent.performance -= 1
                self.update_agent_alive(agent)
            elif (action == "Eat"): #or action == "Drink"):
                #agent.consume(action, self.status[agent.location])
                #self.update_agent_alive(agent) #because consume changes performance without checking agent alive status after
                # vvv old code I used before altering cat class
                if (self.status[agent.location] == "Milk"):
                    agent.performance -= 1
                    self.update_agent_alive(agent)
                elif (self.status[agent.location] == "Sausage"):
                    agent.consume("Sausage")
                    self.status[agent.location] = "Empty"
                else:
                    agent.performance -= 1
                    self.update_agent_alive(agent)
            elif (action == "Drink"):
                if (self.status[agent.location] == "Sausage"):
                    agent.performance -= 1
                    self.update_agent_alive(agent)
                elif (self.status[agent.location] == "Milk"):
                    agent.consume("Milk")
                    self.status[agent.location] = "Empty"
                else:
                    agent.performance -= 1
                    self.update_agent_alive(agent)
            else:
                agent.performance -= 1

    def add_thing(self, thing):
        thing.location = random.choice((loc_A, loc_B))
        if thing in self.agents:
          print("Can't add the same agent twice")
        else:
          if isinstance(thing, Agent):
            thing.performance = 2
            #thing.location = location if location is not None else self.default_location(thing)
            self.agents.append(thing)