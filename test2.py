import numpy as np
import state_machine as sm

z = (np.pi) / 8
u_b = np.array([[1, 0],
                [0, 1]])
u_a = np.array([[np.cos(z), -np.sin(z)],
                [np.sin(z), np.cos(z)]])

init_state = [[1],[0]]
receiving_state = [[1],[0]]
word = np.array([0,0]) #example word
dicti = {0: u_a, 1: u_b}
num_states = 2

state_machine = sm.StateMachine(dicti, num_states, init_state, receiving_state)

result = state_machine.transfer(word)
print(result)