from mesa import Agent, Model
from mesa.time import RandomActivation
from enum import Enum
import networkx as nx
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector

class State(Enum):
    SUSCEPTIBLE = 0
    ACTIVE = 1
    RESISTANT = 2

def number_state(model, state):
    return sum([1 for a in model.grid.get_all_cell_contents() if a.status is state])


def number_infected(model):
    return number_state(model, State.ACTIVE)


def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)


def number_resistant(model):
    return number_state(model, State.RESISTANT)

class PeopleAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, limit_time, model):
        super().__init__(unique_id, model)
        self.time = 0
        self.status = State.SUSCEPTIBLE
        self.limit_time = limit_time

    def step(self):
        if self.status == State.ACTIVE:
            #Infect
            other_agent = self.random.choice(self.model.schedule.agents)
            if other_agent.status == State.SUSCEPTIBLE:
                other_agent.status = State.ACTIVE
            #Cure
            self.time = self.time + 1
            if self.time >= self.limit_time:
                self.time = 0
                self.status = State.RESISTANT

class InfectModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, limit_time, infected_init, neighbors):
        self.num_agents = N
        prob = neighbors / self.num_agents
        self.G = nx.erdos_renyi_graph(n=self.num_agents, p=prob)
        self.grid = NetworkGrid(self.G)
        self.schedule = RandomActivation(self)

        self.datacollector = DataCollector(
            {
                "Infected": number_infected,
                "Susceptible": number_susceptible,
                "Resistant": number_resistant,
            }
        )

        # Create agents
        for i, node in enumerate(self.G.nodes()):
            a = PeopleAgent(i,limit_time, self)
            self.schedule.add(a)
            # Add the agent to the node
            self.grid.place_agent(a, node)

        # Infect some nodes
        infected_nodes = self.random.sample(self.G.nodes(), infected_init)
        for a in self.grid.get_cell_list_contents(infected_nodes):
            a.status = State.ACTIVE
        
        self.datacollector.collect(self)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
        #collecting data
        self.datacollector.collect(self)