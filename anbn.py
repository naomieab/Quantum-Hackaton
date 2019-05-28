import numpy as np
import state_machine as sm

z = (np.pi) * np.sqrt(2)

u_a = np.array([[np.cos(z), -np.sin(z), 0, 0],
                [np.sin(z), np.cos(z), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])


u_b = np.array([[np.cos(-z), -np.sin(-z), 0, 0],
                [np.sin(-z), np.cos(-z), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]])

init_state = [[1],[0],[0],[0]]
receiving_state = [[1],[0],[0],[0]]
word = np.array([0,1,0,1,0]) #example word
dicti = {0: u_a, 1: u_b}
num_states = 2
cutoff = 0.8

state_machine = sm.StateMachine(dicti, num_states, init_state, receiving_state, cutoff)

result = state_machine.transfer(word)
print(result)