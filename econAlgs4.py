"""
this is a submission for question 5.
name: Guy Wolf
ID: 212055966
"""

class Agent:
    def item_value(self, item_index):
        pass

def EF1Singular(agent1, bundle1, agent2, bundle2):
    #values[i][j] = how agent i+1 values bundle j+1
    values = [[0,0],[0,0]]

    for item in bundle1:
        values[0][0] += agent1.item_value(item)
        values[1][0] += agent1.item_value(item)

    for item in bundle2:
        values[0][1] += agent1.item_value(item)
        values[1][1] += agent1.item_value(item)

    if values[0][1] >= values[0][0]:
        #check maximum difference between bundles for a single item
        maxVal = -float("inf")
        for item in bundle1:
            test = agent1.item_value(item)-agent2.item_value(item)
            if test > maxVal:
                maxVal = test
        if values[0][1]-values[0][0]>maxVal:
            return False

    if values[1][0] >= values[1][1]:
        #check maximum difference between bundles for a single item
        maxVal = -float("inf")
        for item in bundle2:
            test = agent2.item_value(item)-agent1.item_value(item)
            if test > maxVal:
                maxVal = test
        if values[1][0]-values[1][1]>maxVal:
            return False

    return True

def is_EF1(agents, bundles):
    numAgents = len(agents)
    for i in range(numAgents):
        for j in range(i, numAgents):
            if not EF1Singular(agents[i], bundles[i], agents[j], bundles[j]):
                return False
    return True

class TestAgent(Agent):
    def __init__(self, values):
        self.values = values

    def item_value(self, item_index):
        return self.values[item_index]

        
    
