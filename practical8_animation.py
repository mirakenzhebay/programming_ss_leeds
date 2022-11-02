# -*- coding: utf-8 -*-
"""
In this code,
1) we animate our model using matplotlib.animation
2) implement stopping condition based on how much the agent stores (the sheep has eaten)
3) further improve the model by adding Offspring class (inherits the functionalities of 
the Agent) and Wolf class with functionalities to interact with other objects

@author: Mira
version: 1.0
"""

import random
from unittest import skip
import matplotlib.pyplot
import matplotlib.animation 
import agentframework   # module that stores Agent class
import csv

# Custom functions
def gen_function(b = []):
    """
    Generator function to provide information to update function in every frame.
    """
    global carry_on 
    while carry_on :
        yield num_of_iterations		
        	
def update(frame_number):
    """
    The function called in every frame, which will take the following actions: 
    - make the agents interact with the environment(move around) and with each other 
    - evaluate conditions for stopping - if met animation stops
    - plot environment and agents, wolves and offsprings 
    """

    fig.clear() 
    global carry_on

    # Set interactions
    ## Agents
    random.shuffle(agents) #shuffle to avoid artifacts
    for i in range(len(agents)):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(agents)
        agents[i].make_offspring(offsprings) 
    
    ## Offsprings
    random.shuffle(offsprings) #shuffle to avoid artifacts
    for i in range(len(offsprings)):
        offsprings[i].move()
        offsprings[i].eat()

    ## Wolves
    random.shuffle(wolves) #shuffle to avoid artifacts
    for i in range(len(wolves)):
        wolves[i].move()
        wolves[i].eat_agents(agents)
        wolves[i].eat_offsprings(offsprings)
        wolves[i].eat()

    # Stopping conditions
    if len(agents) == 0:
        carry_on = False
        print("stopping condition met - all agents are eaten!")   

    if len(offsprings) > 20:
        carry_on = False
        print("stopping condition met - too many lambs!")
    
    #Set the window    
    matplotlib.pyplot.ylim(0, len(environment[1])) #y-axis limit
    matplotlib.pyplot.xlim(0, len(environment[0])) #x-axis limit
    matplotlib.pyplot.ylabel('Y')
    matplotlib.pyplot.xlabel('X')
    matplotlib.pyplot.title('AGENT BASED MODEL')
    matplotlib.pyplot.imshow(environment)
    
    # Plot agents, wolfs, offsprings as scatter points
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, s = 50,  c = 'white', label = 'agents')
    for i in range(len(wolves)):
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, s = 70, c = 'black', marker = 'v', label = 'wolves')
    for i in range(len(offsprings)):
        matplotlib.pyplot.scatter(offsprings[i].x, offsprings[i].y, c = 'red', label = 'offsprings') 

# Create a figure,set size and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make boolean to control the animation using stopping conditions
carry_on = True 

# Open environment data file
in_data=open('data.txt', newline='')
reader = csv.reader(in_data, quoting=csv.QUOTE_NONNUMERIC)

# Fill 'environment' list with the data
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
in_data.close() 

# Create list of agents, offsprings, wolves
agents = []
offsprings = []
wolves = []

# Set number of agents, iterations,neighbourhood
num_of_agents = 20
num_of_wolves = 10
num_of_iterations = 1000
neighbourhood = 30

# Create the agents 
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents, environment, neighbourhood))
    #print("Agents' initial coords:", agents[i]) #check the starting locations of the agents

# Create the wolves
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(i, wolves, environment,neighbourhood))

# Animate
animation = matplotlib.animation.FuncAnimation(fig, update,frames=gen_function, repeat=False)
matplotlib.pyplot.show()

# Write out the resulting environment to file
dataout = open('dataout.txt', 'w', newline='') 
writer = csv.writer(dataout, delimiter=',')
for row in environment:		
	writer.writerow(row)
dataout.close()

