import os
import numpy as np
import random

# Epsilon greedy algorithm
def epsilon_greedy(self, purpose):
    if np.random.rand() < = self.epsilon:  
        return random_choice
    else:
        return purpose_action
# if we set epsilon as 0.4 then we choose purpose_action as 60% 
# and we choose random_action as 40%