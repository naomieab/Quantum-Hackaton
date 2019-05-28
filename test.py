import numpy as np
import state_machine as sm

u_1 = np.identity(4)
u_0 = np.array([[0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0],
                [0, 1, 0, 0]
                ])

init_state = [[1],[0],[0],[0]]
receiving_state = [[1],[0],[0],[0]]
word = np.array([1,1]) #example word
dicti = {0: u_0, 1: u_1}
num_states = 2
cutoff = 0.95

state_machine = sm.StateMachine(dicti, num_states, init_state, receiving_state, cutoff)

result = state_machine.transfer(word)
print(result)