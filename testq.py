import numpy as np
import state_machine as sm
from QuantumStateMachine import QuantumStateMachine
u_1 = np.identity(4)
u_0 = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

init_state = [[1],[0], [0], [0]]
receiving_state = [[1],[0],[0],[0]]
word = np.array([0, 0]) # example word
dicti = {0: u_0, 1: u_1}
num_states = 2


#state_machine = sm.StateMachine(dicti, num_states, init_state, receiving_state)
state_machine = QuantumStateMachine(dicti, num_states, init_state, receiving_state)


result = state_machine.transfer(word)
print(result)