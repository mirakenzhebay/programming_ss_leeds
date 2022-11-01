# -*- coding: utf-8 -*-
"""

This code gives example of how to build a function. We build function to calculate distance between agents. 
Then with the for-loop we find the maximum distance between a pair of agents from the list. Also we time the code
to check how long it takes to run it.

@author: Mira
version: 1.0
"""

#import libraries
import random
import operator
import matplotlib.pyplot
import time

#custom function(s)
def distance_between(agents_row_a, agents_row_b):
    """
    This function calculates the distance between two agents

    Parameters
    ----------
    agents_row_a : double
        The x and y coord-s of agent #1.
    agents_row_b : list
        The x and y coord-s of agent #2.

    Returns
    Pythagorean distance between two passed agents
    TYPE float 

    """
    return (((agents_row_a[0] - agents_row_b[0])**2) +
    ((agents_row_a[1] - agents_row_b[1])**2))**0.5

    
#check how long it takes to run code
start = time.process_time()

# Create an empty list of agents
agents=[]

#Set number of agents
num_of_agents = 100

#Create 100 agents with their random coord-s
for i in range(num_of_agents):
    agents.append([random.randint(0,100),random.randint(0,100)])


#Move the agents around for number of iterations
num_of_iterations=100
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
        #Torus - addressing boundary issue
        if random.random() < 0.5:
            agents[i][0] = (agents[i][0] + 1) % 100
        else:
            agents[i][0] = (agents[i][0] - 1) % 100

# Calculating the Pythagorean distance between the agents 
distance = distance_between(agents[0], agents[1])
print("Distance between first two agents: ",distance)


#Test distance between agents
maxdistance=0
for i in range(num_of_agents):
    for j in range(i+1,num_of_agents):  #use 'i+1' to avoid distance calculation from and to the same agent
        #print(i,j) 
        distance=distance_between(agents[i],agents[j])
        if distance>maxdistance:
            maxdistance=distance
            maxxy=(agents[i],agents[j])
            print(maxxy)
            print(distance)
print('Max distance between two agents from the list:', maxdistance)
       
#Find the  furthest east agent (larger x)
#maxx=max(agents, key=operator.itemgetter(1))

#Plot the agents
# matplotlib.pyplot.ylim(0, 99)
# matplotlib.pyplot.xlim(0, 99)
# for i in range(num_of_agents):
#        matplotlib.pyplot.scatter(agents[i][1],agents[i][0])
# #matplotlib.pyplot.scatter(maxx[1], maxx[0], color='red')
# matplotlib.pyplot.show()


#Check time taken
end = time.process_time()
print("time = " + str(end - start))
