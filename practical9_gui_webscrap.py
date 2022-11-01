# -*- coding: utf-8 -*-
"""
In this code, we build Graphical User Interface (GUI) for our model to display it with menu to run, 
and perform web scraping - request some data into it from the web.

@author: Mira
version: 1.0
"""

import random
import operator
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import time
import agentframework
import csv
import bs4
import requests



def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1

def update(frame_number):
    """
    Every frame will call the update function, which will take the following actions: 
    make the agents interact with the environment(move around) and with each other - 
    eat and share the storen food
    Conditions for stopping will be evaluated.
    Environment and agents will be plotted 
    """

    fig.clear() 
    global carry_on

    for j in range(num_of_iterations):
        random.shuffle(agents) #shuffle to avoid artifacts
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].share_with_neighbours(neighbourhood)
            agents[i].make_offspring(neighbourhood, offsprings) 
    
    #make offsprings move and eat
    for offspring in offsprings:
        offspring.move()
        offspring.eat()

    #make wolves move and eat agents, offsprings and each other
    for wolf in wolves:
        wolf.move()
        #wolf.eat_agents(neighbourhood, wolves, agents)
        wolf.eat_offsprings(neighbourhood, wolves, offsprings)
        wolf.eat()

    #stopping condition
    # for i in range(num_of_agents):
    #     if agents[i].store < 20:
    #         carry_on = False
    #         print("stopping condition met - agent stores more than 70!")
    
    if len(agents) == 0:
        carry_on = False
        print("stopping condition met - no agent left!")        
        
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)

    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, c = 'white', label = 'agents')
        #print(agents[i].x, agents[i].y) 
    for wolf in wolves:
        matplotlib.pyplot.scatter(wolf.x, wolf.y, s = 70, c = 'black', marker = 'v', label = 'wolves')
    for offspring in offsprings:
        matplotlib.pyplot.scatter(offspring.x, offspring.y, c = 'blue', label = 'offsprings') 


#create a figure,set size and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


carry_on = True 

#open environment data file
in_data=open('data.txt', newline='')
reader = csv.reader(in_data, quoting=csv.QUOTE_NONNUMERIC)

#fill 'environment' list with the data
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
in_data.close() 

# create list of agents, offsprings, wolves
agents = []
offsprings = []
wolves = []
#Set number of agents, iterations,neighbourhood
num_of_agents = 10
num_of_wolves = 5
num_of_iterations=100
neighbourhood=20


#Get x, y from web
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
tdsy = soup.find_all(attrs={"class" : "y"})
tdsx = soup.find_all(attrs={"class" : "x"})

#create agents with their random coord-s
for i in range(num_of_agents):
    y = int(tdsy[i].text)
    x = int(tdsx[i].text)
    agents.append(agentframework.Agent(i, environment, agents, x, y))
    #print("Agents' initial coords:", agents[i]) #check the starting locations of the agents

# create the wolves
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(i, environment,
                                       neighbourhood))

root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Just showing menu elements
root = tkinter.Tk()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

tkinter.mainloop() # Wait for interactions.

#r = requests.get('file:///C:/PhD_DA/year1/GEOGR/practicals/data.html', auth=('user', 'pass'))

#for td in tdsy:
#    print (td.text)


