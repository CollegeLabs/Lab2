from src.locations import *
from src.CompanyEnvironmentClass import CompanyEnvironment
from src.Task3YourClasses import Student, ITStaff, OfficeManager
from src.agents import ReflexAgentA2pro
import streamlit as st

locations=loc_A, loc_B, loc_C, loc_D
locations

ce=CompanyEnvironment()
s=Student()
i=ITStaff()
o=OfficeManager()

ce.add_thing(i)
print("IT is located at {}.".format(i.location))
st.write("IT is located at {}.".format(i.location))

ce.add_thing(s)
print("Student is located at {}.".format(s.location))
st.write("Student is located at {}.".format(s.location))

ce.add_thing(o)
print("OfficeManager is located at {}.".format(o.location))
st.write("OfficeManager is located at {}.".format(o.location))

ce.things

raTask3pro1=ReflexAgentA2pro()

ce.add_thing(raTask3pro1)

print("State of the Office Environment: {}.".format(ce.locations))
print("Agent is located at {}.".format(raTask3pro1.location))

st.write("State of the Office Environment: {}.".format(ce.locations))
st.write("Agent is located at {}.".format(raTask3pro1.location))

ce.run()