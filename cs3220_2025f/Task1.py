import random
import collections
import streamlit as st
from src.locations import *
from src.thingClass import Thing
from src.agentClass import Agent
from src.agents import *
from src.CrazyHouseEnvironment import CrazyHouseEnvironment
from src.Task3YourClasses import Milk, Mouse, Dog

def RandomAgentProgram(actions):
   return lambda percept: random.choice(actions)

actions = ['Move_Right', 'Move_Left', 'Eat', 'Drink', 'Fight']

House = CrazyHouseEnvironment()

Cat=RandomCatAgent()

Milk=Milk()
Mouse=Mouse()
Dog=Dog()

House.add_thing(Milk)
House.add_thing(Mouse)
House.add_thing(Dog)


while True:
    if Dog.location == Mouse.location:
        House.delete_thing(Mouse)
        House.add_thing(Mouse)
    if Dog.location != Mouse.location:
        break

if Milk.location == Mouse.location:
    House.delete_thing(Milk)

House.add_thing(Cat)
st.write("Cat is located at {}.".format(Cat.location))

House.run()

