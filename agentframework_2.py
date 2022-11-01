# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 16:43:02 2022

@author: Meruyert
"""
import random

random.seed(0)

class Agent():
    def __init__(self,agents):
        self.x = random.randint(0,99) #x coordinates
        self.y = random.randint(0,99) #y coordinates
    def __str__(self):
        return  "x=" + str(self.x)  + ", y=" + str(self.y)    
    def move(self):
        if random.random() < 0.5:
                self.y = (self.y + 1) % 100
        else:
                self.y = (self.y - 1) % 100
    
        if random.random() < 0.5:
                self.x = (self.x  + 1) % 100
        else:
                self.x  = (self.x - 1) % 100    

        

   