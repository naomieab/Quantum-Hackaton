import numpy as np
import state_machine as sm

z = (np.pi) * np.sqrt(2)

Rx = np.array([[1, 0, 0, 0],
                [0, np.cos(z), -np.sin(z), 0],
                [0, np.sin(z), np.cos(z), 0],
                [0, 0, 0, 1]])

Ry = np.array([[np.cos(z), 0, np.sin(z), 0],
                [0, 1, 0, 0],
                [-np.sin(z), 0, np.cos(z), 0],
                [0, 0, 0, 1]])

u_a = Rx @ Ry

u_b = np.array([[1, 0, 0, 0],
                [0, np.cos(-z), -np.sin(-z), 0],
                [0, np.sin(-z), np.cos(-z), 0],
                [0, 0, 0, 1]])

u_c = np.array([[np.cos(-z), 0, np.sin(-z), 0],
                [0, 1, 0, 0],
                [-np.sin(-z), 0, np.cos(-z), 0],
                [0, 0, 0, 1]])


init_state = [[1],[0],[0],[0]]
receiving_state = [[1],[0],[0],[0]]
word = np.array([0,0,0,1,1,1,2,2,2]) #example word
dicti = {0: u_a, 1: u_b, 2: u_c}
num_states = 2
cutoff = 0.9

state_machine = sm.StateMachine(dicti, num_states, init_state, receiving_state, cutoff)

result = state_machine.transfer(word)
print(result)