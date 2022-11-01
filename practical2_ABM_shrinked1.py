# -*- coding: utf-8 -*-
"""

This piece of code shrinks the code from practical 1 by introducing containers, namely lists.
So the agents' coordinates pairs are now stored in the individual list which form nested list 
of all agents - [[y0,x0], [y1,x1]]

@author: Meruyert
version: 1.0
"""

import random
import operator
import matplotlib.pyplot


# Create empty list of agents
agents=[]

#Append coordinates of agent 1 to the list
agents.append([random.randint(0,99),random.randint(0,99)])

#Move the agent 1 around based on random value
random_num=random.random()

# y coordinates
if random_num < 0.5:
     agents[0][0] += 1
else:
     agents[0][0] -= 1
     
# x coordinates
if random_num < 0.5:
     agents[0][1] += 1
else:
     agents[0][1] -= 1


# Add agent 2 coordinates
agents.append([random.randint(0,99),random.randint(0,99)])
#print(agents)


#Move the agent 2 around based on random value
random_num=random.random()

if random_num < 0.5:
     agents[1][0] += 1
else:
     agents[1][0] -= 1
     

if random_num < 0.5:
     agents[1][1] += 1
else:
     agents[1][1] -= 1

# Calculate the Pythagorean distance between the agents 

dist = (((agents[0][0]- agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
#print("Distance between agents: ", round(dist,2))

#Find the  furthest east agent (larger x)
maxx=max(agents, key=operator.itemgetter(1))
#print(maxx)

#Plot the agent locations
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(maxx[1], maxx[0], color='green') #plot the furthest east agent in green
matplotlib.pyplot.show()