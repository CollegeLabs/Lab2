from src.task2Classes import *
from src.task2Environment import *
from src.agentPrograms import TableDrivenAgentProgram
house = CatFriendlyHouseEnvironment()
feedingRules = {(((0, 0), 'Empty'),): 'Right',
 (((0, 0), 'Milk'),): 'Drink',
 (((0, 0), 'Sausage'),): 'Eat',
 (((1, 0), 'Empty'),): 'Left',
 (((1, 0), 'Milk'),): 'Drink',
 (((1, 0), 'Sausage'),): 'Eat',
 (((0, 0), 'Milk'), ((0, 0), 'Empty')): 'Right',
 (((0, 0), 'Sausage'), ((0, 0), 'Empty')): 'Right',
 (((0, 0), 'Empty'), ((1, 0), 'Milk')): 'Drink',
 (((0, 0), 'Empty'), ((1, 0), 'Sausage')): 'Eat',
 (((1, 0), 'Empty'), ((0, 0), 'Milk')): 'Drink',
 (((1, 0), 'Empty'), ((0, 0), 'Sausage')): 'Eat',
 (((1, 0), 'Milk'), ((1, 0), 'Empty')): 'Left',
 (((1, 0), 'Sausage'), ((1, 0), 'Empty')): 'Left',
 (((0, 0), 'Milk'), ((0, 0), 'Empty'), ((1, 0), 'Milk')): 'Drink',
 (((0, 0), 'Milk'), ((0, 0), 'Empty'), ((1, 0), 'Sausage')): 'Eat',
 (((0, 0), 'Sausage'), ((0, 0), 'Empty'), ((1, 0), 'Milk')): 'Drink',
 (((0, 0), 'Sausage'), ((0, 0), 'Empty'), ((1, 0), 'Sausage')): 'Eat',
 (((1, 0), 'Milk'), ((1, 0), 'Empty'), ((0, 0), 'Milk')): 'Drink',
 (((1, 0), 'Milk'), ((1, 0), 'Empty'), ((0, 0), 'Sausage')): 'Eat',
 (((1, 0), 'Sausage'), ((1, 0), 'Empty'), ((0, 0), 'Milk')): 'Drink',
 (((1, 0), 'Sausage'), ((1, 0), 'Empty'), ((0, 0), 'Sausage')): 'Eat'}

a1=Cat(feedingRules)
house.add_thing(a1)
print("State of the Environment: {}.".format(house.status))
print("Agent is located at {}.".format(a1.location))
print(house.agents)
print(house.agents[0].location)
house.run()