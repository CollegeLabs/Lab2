from src.task2Classes import *
from src.task2Environment import *

a1 = Cat()
house = CatFriendlyHouseEnvironment()
house.add_thing(a1)
a1.location = random.choice([loc_A, loc_B])
house.run()
#feedingRules = {}