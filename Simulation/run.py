from local_library import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math

n = 1000 #How many individuals will be in the world
it = 100 #How many iterations of the algorithm
samples = 5 #How many samples of the algorithm will be considered
limit_time = 5 #How many interactions the person remain infected
infected_init_perc = 0.1 #Initial infected percentage (if it is bigger than n, it is considered 10% infected)
neighbors = 2 #How many neighbors, in average, for person 


#Defining initial infected number
infected_init = math.floor(infected_init_perc * n)
if(infected_init > n):
    infected_init = math.floor(0.1 * n)

all_infected = pd.DataFrame()
#This runs the model samples times, each model executing it steps.
for j in range(samples):
    #Run model
    model = InfectModel(n, limit_time, infected_init, neighbors)

    #Interactions
    for i in range(it):
        model.step()

    #Collect data
    data = model.datacollector.get_model_vars_dataframe()
    all_infected = all_infected.append(data.loc[:,"Infected"], ignore_index=True)

#all_infected has each row being samples and data in columns. So we have to transpose in order to plot it
all_infected.transpose().plot()
plt.show()
