# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 18:04:13 2022

This code introduces the basic steps to build agent-based model(ABM). The two agents are created and their
y and x coordinates are set. They both begin at the same spot and move forward using random numbers. 
The final step is to compute the distance  between the agents.

@author: Mira
version: 1.0
"""

# import libraries
import random


## AGENT 1
# Set Agent 1 coordinates
y0=50
x0=50

#Set random value for moving agent 1 around
random_num=random.random()
#print(random_num)

#Move the agent 1 around, step #1
if random_num < 0.5:
     y0 += 1
else:
     y0 = y0 - 1

if random_num < 0.5:
     x0 += 1
else:
     x0 = x0 - 1
print("Agent #1 coord-s after first step:", "x0 -", x0,", y0 -",y0)

#Move the agent 1 around, step #2
if random_num < 0.5:
     y0 += 1
else:
     y0 = y0 - 1
if random_num < 0.5:
     x0 += 1
else:
     x0 = x0 - 1
print("Agent #1 coord-s after second step:",  "x0 -", x0,", y0 -",y0)


## AGENT 2
# Set Agent 2 coordinates
y1=50
x1=50

#Set random value for moving agent 2 around
random_num=random.random()

#Move the agent 2 around, step #1
if random_num < 0.5:
     y1 += 1
else:
     y1 = y1 - 1
if random_num < 0.5:
     x1 += 1
else:
     x1 = x1 - 1
print("Agent #2 coord-s after first step:",  "x1 -", x1,", y1 -",y1)

#Move the agent 2 around,  step #2
if random_num < 0.5:
     y1 += 1
else:
     y1 = y1 - 1
if random_num < 0.5:
     x1 += 1
else:
     x1 = x1 - 1
print("Agent #2 coord-s after second step:",  "x1 -", x1,", y1 -",y1)


# Calculate the Pythagorean distance between the agents 
dist = (((y0 - y1)**2) + ((x0 - x1)**2))**0.5
print("Distance between agents: ", round(dist,2))