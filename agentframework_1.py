# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:43:02 2022

@author: Meruyert
"""
import random

random.seed(0)

class Agent():
    def __init__(self, i, environment, agents, neighbourhood, y, x):
        self.i=i
        self.y=y
        self.x = x
        self.environment = environment
        self.agents=agents
        self.agent =[a for a in agents]
        self.neighbourhood = neighbourhood
        self.store = 0 
        if (x == None):
           self._x = random.randint(0,100)
        else:
           self._x = x

    def __str__(self):
        return "i = " +str(self.i)+", store = " + str(self.store) + ", x=" + str(self.x) \
                + ", y=" + str(self.y) 
    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
                self.environment[self.y][self.x] -= 10
                self.store += 10
        else:
                self.store+=self.environment[self.y][self.x]
                self.environment[self.y][self.x] = 0
        if self.store >= 100:
                self.environment[self.y][self.x] += self.store
                self.store=0
        
    def move(self):
        if random.random() < 0.5:
                self.y = (self.y + 1) % 100
        else:
                self.y = (self.y - 1) % 100
    
        if random.random() < 0.5:
                self.x = (self.x  + 1) % 100
        else:
                self.x  = (self.x - 1) % 100    
    
    def distance_between(self, agent):
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
     return (((self.x - agent.x)**2) +((self.y - agent.y)**2))**0.5


    def share_with_neighbours(self,neighbourhood):
        for i in range(len(self.agents)):

              distance = self.distance_between(self.agents[i])
              if distance <= neighbourhood:
                   av= (self.store + self.agents[i].store)/2
                   self.store=av
                   self.agents[i].store = av
                   print("agents are sharing " + str(distance) + " "+str(av))
              else: 
                   pass 
    
    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y

    def get_x(self):
        print(str(self.x))
    def get_y(self):
        print(str(self.y))

        

   