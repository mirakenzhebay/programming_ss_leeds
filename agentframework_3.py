# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:43:02 2022

@author: Meruyert
"""
import random

random.seed(0)

class Agent():
    def __init__(self,i, environment, agents):
        self.i=i
        self.x = random.randint(0,99) #x coordinates
        self.y = random.randint(0,99) #y coordinates
        self.environment = environment
        self.agents=agents
        self.store = 0 
        
    def __str__(self):
        return "agent_id = " +str(self.i)+", store = " + str(self.store) + ", x=" + str(self.x) \
                + ", y=" + str(self.y) 
    def eat(self): 
        if self.environment[self.y][self.x] > 10:   #if there's more than 10 left, eat 10 and store it
                self.environment[self.y][self.x] -= 10
                self.store += 10 
        else:
                self.store+=self.environment[self.y][self.x]   #if there's less than 10 left, eat all of it and leave empty
                self.environment[self.y][self.x] = 0
        if self.store >= 100:
                self.environment[self.y][self.x] += self.store #if there's more than/equal to 100 left, agent returns everything stored back
                self.store=0                                   #and stores nothing
        
    def move(self):
        if random.random() < 0.5:
                self.y = (self.y + 1) % 100
        else:
                self.y = (self.y - 1) % 100
    
        if random.random() < 0.5:
                self.x = (self.x  + 1) % 100
        else:
                self.x  = (self.x - 1) % 100    
    
    def distance_between(self, agents):
     """
    This function calculates the distance between two agents
     """
     return (((self.x - agents.x)**2) +((self.y - agents.y)**2))**0.5

    def share_with_neighbours(self,neighbourhood):
        for i in range(len(self.agents)):
            if self != self.agents[i]:
              if self.distance_between(self.agents[i]) <= neighbourhood:
                   average= (self.store + self.agents[i].store)/2
                   self.store=average
                   self.agents[i].store = average
                   #print("agents in a distance of " + str(round(distance,2)) 
                   #+ " shared their food and now have "+str(round(average,2))+ " units each")
    
    def make_offspring(self,neigbourhood, offsprings):
        for i in range(len(self.agents)):
            if self != self.agents[i]:
                if self.distance_between(self.agents[i]) <= 2:
                    offsprings.append(Offspring(i, self.environment, neigbourhood))

    def set_x(self,x):
        self.x=x
    def set_y(self,y):
        self.y=y

    def get_x(self):
        print(str(self.x))
    def get_y(self):
        print(str(self.y))


class Offspring(Agent):

    """
    Offspring class inherits behaviour from Agent class
    """
    def __init__(self, i, environment, agents):
        super().__init__(i, environment, agents)


class Wolf(Agent):
    """"
    Wolf class inherits the behaviour from Agent class
    but also has additional functionalities - eat not only their own
    but also agents and offsprings
    """
    def __init__(self, i, environment, agents):
        super().__init__(i, environment, agents)

    def eat_agents(self, neighbourhood, wolves, agents):
        for _wolf in wolves:
            for agent in agents:
                distance = self.distance_between(agent) 
                if distance <= neighbourhood:
                    # wolf aquires agents store and removes agent
                    self.store += agent.store
                    agents.remove(agent)
                

    def eat_offsprings(self, neighbourhood, wolves, offsprings):
        for wolf in wolves:
            for offspring in offsprings:
                distance = self.distance_between(offspring) 
                if distance <= neighbourhood:
                    self.store += offspring.store #wolf gets what offspring stores and eats it
                    offsprings.remove(offspring)