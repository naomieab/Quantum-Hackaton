import numpy as np
from QuantumStateMachine import QuantumStateMachine

z = (np.pi) / 2
u_b = np.identity(4)
u_a = np.array([[np.cos(z), -np.sin(z), 0, 0],
                [np.sin(z), np.cos(z), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

init_state = [[1],[0],[0],[0]]
receiving_state = [[1],[0],[0],[0]]
word = np.array([0]*4) #example word
dicti = {0: u_a, 1: u_b}
num_states = 2
cutoff = 0.9

state_machine = QuantumStateMachine(dicti, num_states, init_state, receiving_state, cutoff)

result = state_machine.transfer(word)
print(result)