from local_library import *
import matplotlib.pyplot as plt
import math

n = 1000 #How many individuals will be in the world
it = 100 #How many iterations of the algorithm
samples = 10 #How many samples of the algorithm will be considered NOT USED NOW
limit_time = 3 #How many interactions the person remain infected
infected_init_perc = 0.1 #Initial infected percentage (if it is bigger than n, it is considered 10% infected)
neighbors = 2 #How many neighbors, in average, for person 


#Defining initial infected number
infected_init = math.floor(infected_init_perc * n)
if(infected_init > n):
    infected_init = math.floor(0.1 * n)

model = InfectModel(n, limit_time, infected_init, neighbors)

for i in range(it):
    model.step()
print(model.datacollector.get_model_vars_dataframe())

model.datacollector.get_model_vars_dataframe().plot()
plt.show()

# #BEGIN TO HELP MULTIPLE INTERACTIONS
# all_status = []
# #This runs the model samples times, each model executing it steps.
# for j in range(samples):
#     # Run the model
#     model = InfectModel(n, limit_time, infected_init, neighbors)
#     for i in range(it):
#         model.step()

#     # Store the results
#     for agent in model.schedule.agents:
#         all_status.append(agent.status)

# print(all_status)