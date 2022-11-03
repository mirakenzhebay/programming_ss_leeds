# -*- coding: utf-8 -*-
"""
(Practical 9)
In this code, we build Graphical User Interface (GUI) for our model to display it with menu to run, 
and perform web scraping - request some data into it from the web.

@author: Mira
version: 1.0
"""

import random
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agentframework
import csv
import bs4
import requests
import urllib3
import sys


#if model parameters given
if len(sys.argv) == 5:
    while True:
        try:
            # run model with provided parameters
            num_of_agents = int(sys.argv[1])
            num_of_wolves = int(sys.argv[2])
            neighbourhood = int(sys.argv[3]) 
            num_of_iterations = int(sys.argv[4])
            print('Running the model with the following param-s',
            num_of_agents, ' agents, ', num_of_wolves,' wolves, ',
            'in a neighbourhood distance equal to ', neighbourhood, 
             ' units, for',  num_of_iterations, ' iterations', )
            break
        except ValueError:
            # else, revert to sys_args function
            print("Parameters must be passed as integers")
            break


# if no model parameters given, use default
elif len(sys.argv) == 1:
    num_of_agents = 10
    num_of_wolves = 5
    num_of_iterations = 1000
    neighbourhood = 30
    print('No param-s passed, running the model with the default param-s',
            num_of_agents, ' agents, ', num_of_wolves,' wolves, ',
            'in a neighbourhood distance equal to ', neighbourhood, 
             ' units, for',  num_of_iterations, ' iterations', )    
# If incorrect number of parameters passed
else:
    print("Incorrect number of arguments passed, must be 4 excl.script")

# Custom functions
def run():
    """
    Function used to start the model animation.
    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

def gen_function(b = []):
    """
    Generator function to provide information to update function in every frame.
    """
    global carry_on 
    a=0
    while carry_on and a <= num_of_iterations:
        yield a
        a += 1		

def update(frame_number):
    """
    The function called in every frame, which will take the following actions: 
    - make the agents interact with the environment(move around) and with each other 
    - evaluate conditions for stopping - if met animation stops
    - plot environment and agents, wolves and offsprings 
    """

    fig.clear() 
    global carry_on

    # Set interactions
    ## Agents
    random.shuffle(agents) #shuffle to avoid artifacts
    for i in range(len(agents)):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(agents)
        agents[i].make_offspring(offsprings) 
    
    ## Offsprings
    random.shuffle(offsprings) #shuffle to avoid artifacts
    for i in range(len(offsprings)):
        offsprings[i].move()
        offsprings[i].eat()

    ## Wolves
    random.shuffle(wolves) #shuffle to avoid artifacts
    for i in range(len(wolves)):
        wolves[i].move()
        wolves[i].eat_agents(agents)
        wolves[i].eat_offsprings(offsprings)
        wolves[i].eat()

    # Stopping conditions
    if len(agents) == 0:
        carry_on = False
        print("stopping condition met - all agents are eaten!")   

    if len(offsprings) > 20:
        carry_on = False
        print("stopping condition met - too many lambs!")
    
    #Set the window    
    matplotlib.pyplot.ylim(0, len(environment[1])) #y-axis limit
    matplotlib.pyplot.xlim(0, len(environment[0])) #x-axis limit
    matplotlib.pyplot.ylabel('Y')
    matplotlib.pyplot.xlabel('X')
    matplotlib.pyplot.title('AGENT BASED MODEL')
    matplotlib.pyplot.imshow(environment)
    
    # Plot agents, wolfs, offsprings as scatter points
    for i in range(len(agents)):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y, s = 50,  c = 'white', label = 'agents')
    for i in range(len(wolves)):
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y, s = 70, c = 'black', marker = 'v', label = 'wolves')
    for i in range(len(offsprings)):
        matplotlib.pyplot.scatter(offsprings[i].x, offsprings[i].y, c = 'red', label = 'offsprings') 


# Create a figure,set size and axes
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# Make boolean to control the animation using stopping conditions
carry_on = True 

# Open environment data file
in_data=open('data.txt', newline='')
reader = csv.reader(in_data, quoting=csv.QUOTE_NONNUMERIC)

# Fill 'environment' list with the data
environment = []
for row in reader:
    rowlist = []
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
in_data.close() 

# Create list of agents, offsprings, wolves
agents = []
offsprings = []
wolves = []

# Get web data - x,y coord-s for the agents
urllib3.disable_warnings() # to go around InsecureRequestWarning - not recommended if not sure about the source
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html', verify=False)
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
tdsy = soup.find_all(attrs={"class" : "y"})
tdsx = soup.find_all(attrs={"class" : "x"})

# Create agents 
for i in range(num_of_agents):
    y = int(tdsy[i].text)
    x = int(tdsx[i].text)
    agents.append(agentframework.Agent(i, agents, environment,  x, y))
    #print("Agents' initial coords:", agents[i]) #check the starting locations of the agents

# Create the wolves
for i in range(num_of_wolves):
    wolves.append(agentframework.Wolf(i, wolves, environment, neighbourhood))

# Set up the GUI
root = tkinter.Tk() #build the main window
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root) #create and lay out a matplotlib canvas inside our window
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# Set up the menu
menu_bar = tkinter.Menu(root)
model_menu = tkinter.Menu(menu_bar)
model_menu.add_command(label="Run model", command=run)
menu_bar.add_cascade(label="Model", menu=model_menu)
root.config(menu=menu_bar)
tkinter.mainloop() # waiting for events and updating the GUI





