# -*- coding: utf-8 -*-
"""
In this code, 
1) as in the previous practical we import raster data as our agents' environment 
and let our created agents interact with it-move around it, eat and and store eaten- using 
the Agent class methods stored in agentframework.
2) we let the agents communicate with each other and change each other variables using 
'.share_with_neighbours' method. This method looks for nearest neighbours of agent in specified
distance from it and shares the food with them by splitting their total amount of food equally.
More details of the method are given in the source code - agentframework.py
3) introduce artifacts - patterns or mistakes that result from the model's 
operation, not from how well it represents reality -  and avoid them by randomizing the order=shuffling.

@author: Mira
version: 1.0
"""
#import libraries
import random
import time
import agentframework_3 as agentframework          #containing our new 'Agent' class
import csv                     #to read and write csv files

#check how long it takes to run code
start = time.process_time()

#Open environment data file
in_data=open('data.txt', newline='')
reader = csv.reader(in_data, quoting=csv.QUOTE_NONNUMERIC)

#Fill 'environment' list with the data
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
in_data.close() 

# Create nested list of agents
agents=[]

#Set number of agents, iterations,neighbourhood
num_of_agents = 10
num_of_iterations=100 
neighbourhood=20 #max distance from the agent that is considered its neighbourhood

#Create agents with their random coord-s
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, environment, agents))
    #print("Agents' initial coords:", agents[i]) #check the starting locations of the agents

#Move the agents around, let them eat and share with neighbours the eaten(stored) 
# for number of iterations
for j in range(num_of_iterations):
    random.shuffle(agents) #shuffle to avoid artifacts
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 

#for i in range(num_of_agents):
    #print("Agents' coords after all the actions:", agents[i]) #check the new locations of the agents & how much they store

#Check time
end = time.process_time()
print("time = " + str(end - start))