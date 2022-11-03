# -*- coding: utf-8 -*-
"""

This piece of code shrinks the practical 2 code by introducing control flow statement 'for'. We use it
to create as many agents as we want (num_of_agents), and move them as many times as we like(num_of_iterations). 
Also, in this practical, we show two solutions to address edge issues - the case when the agents move too far away.
First solution is solid wall setting - when the agent moves too far it's coord-s are reset to min boundary/max boundary.
Second solution is torus - if agents moves away at the top/right,  it enters from bottom/left and the opposite/

@author: Meruyert
version: 1.0
"""

import random
import operator
import matplotlib.pyplot

# Create empty list of agents
agents=[]

#Set number of agents
num_of_agents = 10

#Create 100 agents with their random coord-s
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])
#print("Agents coords: ", agents)

#Move the agents around for number of iterations based on random value
num_of_iterations=10

for j in range(num_of_iterations):
    for i in range(num_of_agents):
        
        if random.random() < 0.5:
             agents[i][0] += 1
        else:
             agents[i][0] -= 1
        if random.random() < 0.5:
             agents[i][1] += 1
        else:
             agents[i][1] -= 1
     
     #The below are two techniques to address edge issues 
     #edge issue is when the range is too large
        #1. Solid wall setting
        # if agents[i][0] < 0:
        #     agents[i][0] = 0
        # if agents[i][1] < 0:
        #     agents[i][0] = 0
        # if agents[i][0] > 99:
        #     agents[i][0] = 99
        # if agents[i][1] > 99:
        #     agents[i][1] = 99
        #print(agents[i])
        
        #2. Torus 
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100
    #print("Agents' coord-s at iteration ", j, ":", agents)

"""
Calculate the Pythagorean distance between the agents 
dist = (((agents[0][0]- agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
print("Distance between agents: ", round(dist,2))
"""

#Find the  furthest east agent (larger x)
maxx = max(agents, key=operator.itemgetter(1))
#print("furthest east agent coord-s: " ,maxx)

#Plot the agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylabel('Y')
matplotlib.pyplot.xlabel('X')
matplotlib.pyplot.title('AGENT BASED MODEL')
for i in range(num_of_agents):
       matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
matplotlib.pyplot.scatter(maxx[1], maxx[0], color='green')   #plot the furthest east agent in green
matplotlib.pyplot.show()