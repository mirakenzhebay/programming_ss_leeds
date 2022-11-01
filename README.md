# Programming for Social Sciences, Assignment #1: practicals delivery
This repository includes commented practicals from Programming for Social Sciences module, University of Leeds. The are 9 practicals which are designed to learn how to build simple Agent-based Model. The practicals flow starts from creating agents with their location to making them interact with environment and each other. It also gives introduction on plotting and animating agents and environment. In the end the way how to perform web scraping is given. More details on each practical are provided below.

## Practical 1
In this practical, the two agents are created and their y and x coordinates are set. They both begin at the same spot and move forward using random numbers. The final step is to compute the distance  between the agents.

## Practical 2
In this practical, we shrink the code from practical 1 by introducing containers, namely lists. So, now the agents' coordinates pairs are stored in the individual list which form nested list of all agents - [[y0,x0], [y1,x1]].

## Practical 3
In this practical, we shrink the code from practical 2 by introducing control flow statement 'for'. We use it to create as many agents as we want (num_of_agents), and move them as many times as we like (num_of_iterations).  Also, we show two solutions to address edge issues - the case when the agents move too far away. First solution is solid wall setting - when the agent moves too far it's coord-s are reset to min boundary/max boundary. Second solution is torus - if agents moves away at the top/right,  it enters from bottom/left and the opposite.

## Practical 4
This practical gives example of how to build a function. We build function to calculate distance between agents. Then with the for-loop we find the maximum distance between a pair of agents from the list. Also we time the code to check how long it takes to run it.

## Practical 5
In this practical, we create and move agents around as in the previous practicals. However we make the objects, our agents, by using our template - Agent class - that is stored in the agentframework module and move the agents around using the class method '.move()'. The class has variables - randomly initialized x and y coordinates. Using classes helps to produce clean and easy to maintain code and is useful to build complicated system.

## Practical 6
In this practical, we perform the followings:
1) learn how to load data file - import raster data as our agents' environment;
2) let our created agents interact with it- move around it, eat and and store eaten from the environment - using the Agent class methods stored in agentframework(more details about the methods in agentframework.py)
3) we write out the changed environment to the file. 

## Practical 7
In this practical,  we perform the followings:
1) as in the previous practical we import raster data as our agents' environment and let our created agents interact with it-move around it, eat and and store eaten- using the Agent class methods stored in agentframework.
2) we let the agents communicate with each other and change each other variables using '.share_with_neighbours' method. This method looks for nearest neighbours of agent in specified distance from it and shares the food with them by splitting their total amount of food equally. More details of the method are given in the source code - agentframework.py
3) introduce artifacts - patterns or mistakes that result from the model's operation, not from how well it represents reality -  and avoid them by randomizing the order=shuffling.

## Practical 8
In this practical, we perform the followings:
1) we animate our model using matplotlib.animatiion
2) implement stopping condition based on how much the agent stores (the sheep has eaten)
2) further improve the model by adding Offspring class(inherits the functionalities of the Agent) and Wolf class with functionalities to interact with other objects

## Practical 9
In this practical, we build Graphical User Interface (GUI) for our model to display it with menu to run, and perform web scraping - request some data into it from the web.
