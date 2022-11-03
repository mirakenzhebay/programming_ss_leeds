# -*- coding: utf-8 -*-
"""
 
In this code, 
1) We create and move agents around as in the previous practicals. 
2) However we make the objects, our agents, by using our template - Agent class - that is stored in the agentframework 
module and move the agents around using the class method '.move()'. The class has variables - randomly 
initialized x and y coordinates. Using classes helps to produce clean and easy to maintain code and is
useful to build complicated system.

@author: Mira
version: 1.0
"""

#import libraries
import matplotlib.pyplot
import time
import agentframework  # module that stores Agent class

##custom function(s)
def distance_between(agents_row_a, agents_row_b):
    """
    This function calculates the distance between two agents

    Parameters
    ----------
    agents_row_a : list
        The coord-s of agent #1.
    agents_row_b : list
        The coord-s of agent #2.

    Returns
    distance between two agents
    TYPE float 

    """
    return (((agents_row_a.x - agents_row_b.x)**2) +
    ((agents_row_a.y - agents_row_b.y)**2))**0.5


#check how long it takes to run code
start = time.process_time()

# Create list of agents
agents=[]

#Set number of agents, iterations,neighbourhood
num_of_agents = 10
num_of_iterations=100
neighbourhood=20

#Create 100 agents with their random coord-s using Agent class
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents))   
    # print("Agents' initial coords: agent", agents[i]) #check the starting locations of the agents

#Move the agents around for number of iterations
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()

# for i in range(num_of_agents):
    # print("Agents' coords after moving around: agent", i, agents[i]) #check the new locations of the agents


#Calculate distance between agents
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

#Plot the agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylabel('Y')
matplotlib.pyplot.xlabel('X')
matplotlib.pyplot.title('AGENT BASED MODEL')
for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
matplotlib.pyplot.show()

#Check time
end = time.process_time()
print("time = " + str(end - start))

