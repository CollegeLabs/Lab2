from src.task2Classes import *
from src.task2Environment import *

a1 = Cat()
a1.location = random.choice([loc_A, loc_B])
house = CatFriendlyHouseEnvironment()
house.run()
#feedingRules = {}