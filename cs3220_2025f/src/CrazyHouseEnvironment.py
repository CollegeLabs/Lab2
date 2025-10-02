from src.environmentProClass import environmentPro
from src.thingClass import Thing
from src.locations import *
from src.Task3YourClasses import Milk, Mouse, Dog

import random

class CrazyHouseEnvironment(environmentPro):
  def __init__(self):
    super().__init__()
    self.performace = 5

  def percept(self, agent):
    #return a list of things that are in our agent's location
    things = self.list_things_at(agent.location)
    return agent.location, things
 
  def is_agent_alive(self, agent):
    return agent.alive

  def update_agent_alive(self, agent):
    if agent.performance < 0:
      agent.alive = False
      print("The Cat {} is dead.".format(agent))

  def execute_action(self, agent, action):
    '''Check if agent alive, if so, execute action'''
    if self.is_agent_alive(agent):

        if action == 'Move_Right':
            if agent.location == Room1:
                agent.location = Room2
            elif agent.location == Room2:
                agent.location = Room3
            elif agent.location == Room3:
                agent.location = Room4 
            elif agent.location == Room4:
                agent.location = Room5 
            elif agent.location == Room5:
                agent.location = Room5  
            agent.performance -= 1
            self.update_agent_alive(agent)
        elif action == 'Move_Left':
            if agent.location == Room5:
                agent.location = Room4
            elif agent.location == Room4:
                agent.location = Room3
            elif agent.location == Room3:
                agent.location = Room2 
            elif agent.location == Room2:
                agent.location = Room1 
            elif agent.location == Room1:
                agent.location = Room1  
            agent.performance -= 1
            self.update_agent_alive(agent)
        elif action == 'Eat':
            if self.list_things_at(agent.location, thingClass=Mouse):
                item = self.list_things_at(agent.location, thingClass=Mouse)
                if agent.performance >= 3:
                    agent.performance += 10
                    self.delete_thing(item[0])
                else:
                    agent.performance -= 1
            else:
                agent.performance -= 1
            self.update_agent_alive(agent)
        elif action == 'Drink':
            if self.list_things_at(agent.location, thingClass=Milk):
                item = self.list_things_at(agent.location, thingClass=Milk)
                agent.performance += 5
                self.delete_thing(item[0])
            else:
                agent.performance -= 1
            self.update_agent_alive(agent)
        elif action == 'Fight':
            if self.list_things_at(agent.location, thingClass=Dog):
                item = self.list_things_at(agent.location, thingClass=Dog)
                if agent.performance >= 10:
                    agent.performance += 20
                    self.delete_thing(item[0])
                else:
                    agent.performance -= 10
            else:
                agent.performance -= 1
            self.update_agent_alive(agent)            

  def default_location(self, thing):
        """Thing start in either location at random."""
        print("Thing is starting in random location...")
        return random.choice([Room1, Room2, Room3, Room4, Room5])