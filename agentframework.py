# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:43:02 2022

@author: Meruyert
version: 1.4
"""
import random

random.seed(0)

class Agent():
    """
        Instantiate an agent in an environment.
    
    Attributes:
        i: Agent ID
        environment: A nested list that contains environment data
        x,y: Agent coord-s 
        store: The units the agent have eaten
        neighbourhood: The euclidean distance in which agent interacts with other agents

    """

    def __init__(self,i, agents, environment=None, neighbourhood=None, x=None, y=None):
        self.i=i
        self.agents = agents
        self.environment = environment
        self.neighbourhood = neighbourhood
        self.store = 0 
        if (environment == None):
            self.xmax, self.ymax = 100, 100
        else:
            self.xmax, self.ymax = len(self.environment[0]), len(self.environment[1])
        if (y == None):
            self.y = random.randint(0,self.ymax) #set random y within y-axes of the env
        else:
            self.y = y
        if (x == None):
            self.x = random.randint(0,self.xmax) #set random x within x-axes of the env
        else:
            self.x = x

    def __str__(self):
        return "agent_id = " +str(self.i)+", store = " + str(self.store) + ", x=" + str(self.x) \
                + ", y=" + str(self.y) 

    ## ---------------------- methods ----------------------

    def eat(self): 
        """ Reduce the number of units on specified location in the environment. """
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
        """ Move randomly within an environment. """
        if random.random() < 0.5:
                self.x = (self.x  + 5) % self.xmax
        else:
                self.x  = (self.x - 5) % self.xmax  

        if random.random() < 0.5:
                self.y = (self.y + 5) % self.ymax
        else:
                self.y = (self.y - 5) % self.ymax
    
    def distance_between(self, agents):
        """ Calculate the distance between two agents. """
        return (((self.x - agents.x)**2) +((self.y - agents.y)**2))**0.5

    def share_with_neighbours(self, agents):
        """ Share its store with neighbour evenly. """
        for i in range(len(self.agents)):
            if self != agents[i]:
              if self.distance_between(agents[i]) <= self.neighbourhood:
                   average = (self.store + agents[i].store)/2
                   self.store = average
                   agents[i].store = average
                   #print("agents in a distance of " + str(round(distance,2)) 
                   #+ " shared their food and now have "+str(round(average,2))+ " units each")
    
    def make_offspring(self,  offsprings):
        """ Instantiate an offspring class. """
        for i in range(len(self.agents)):
            if self != self.agents[i]:
                if self.distance_between(self.agents[i]) <= 5:
                    offsprings.append(Offspring(i, offsprings, self.environment, self.neighbourhood))

    def set_x(self,x):
        self._x=x
    def set_y(self,y):
        self._y=y

    def get_x(self):
        print(str(self.x))
    def get_y(self):
        print(str(self.y))


class Offspring(Agent):
    """
    Instantiate an Offspring class that inherits attributes and behaviours from Agent class
    """
    def __init__(self, i, agents, environment=None, neighbourhood=None, x=None, y=None):
        super().__init__(i, agents, environment, neighbourhood, x, y)


class Wolf():
    """
    Instantiate a Wolf class 
    
    Attributes:
        i: Wolf ID
        environment: A nested list that contains environment data
        x,y: Wolf coord-s 
        store: The units the wolf got eating 'grass' from an environment, agents, offsprings
        neighbourhood: The euclidean distance in which agent interacts with other agents

    """

    def __init__(self, i, wolves, environment, neighbourhood):
        self.i=i
        self.wolves = wolves
        self.environment = environment
        self.neighbourhood = neighbourhood
        self.store = 0 
        self.y = random.randint(0, len(self.environment[1]))        
        self.x = random.randint(0, len(self.environment[0]))
        
    def __str__(self):
        return "wolf_id = " +str(self.i)+", store = " + str(self.store) + ", x=" + str(self.x) \
                + ", y=" + str(self.y) 

    ## ---------------------- methods ----------------------
    def eat(self): 
        """ Reduce the number of units on specified location in the environment. """
        if self.environment[self.y][self.x] > 5:   #if there's more than 5 left, eat 5 and store it
                self.environment[self.y][self.x] -= 5
                self.store += 5 
        else:
                self.store+=self.environment[self.y][self.x]   #if there's less than 5 left, eat all of it and leave empty
                self.environment[self.y][self.x] = 0
        if self.store >= 100:
                self.environment[self.y][self.x] += self.store #if there's more than/equal to 100 left, agent returns everything stored back
                self.store=0                                   #and stores nothing
        
    def move(self):
        """ Move randomly within an environment. """
        if random.random() < 0.5:
                self.y = (self.y + 10) % len(self.environment[1])
        else:
                self.y = (self.y - 10) % len(self.environment[1])
    
        if random.random() < 0.5:
                self.x = (self.x  + 10) % len(self.environment[0])
        else:
                self.x  = (self.x - 10) % len(self.environment[0])   
    
    def distance_between(self, prey):
     """ Calculate the distance between wolf and its prey. """
     return (((self.x - prey.x)**2) +((self.y - prey.y)**2))**0.5

    def eat_agents(self, agents):
        """ Remove the neigbouring agent and store what it's eaten. """
        for wolf in self.wolves:
            for agent in agents:
                distance = self.distance_between(agent) 
                if distance <= self.neighbourhood:
                    self.store += agent.store
                    agents.remove(agent)      

    def eat_offsprings(self, offsprings):
        """ Remove the neighbouring offspring and store what it's eaten. """
        for wolf in self.wolves:
            for offspring in offsprings:
                distance = self.distance_between(offspring) 
                if distance <= self.neighbourhood:
                    self.store += offspring.store 
                    offsprings.remove(offspring)
    
    def get_x(self):
        print(str(self.x))
    def get_y(self):
        print(str(self.y))
        