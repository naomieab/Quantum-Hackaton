import numpy as np

class StateMachine():

    def __init__(self, dict, num_states, init_state, receiving_states):
        self.dict = dict
        self.num_states = num_states
        self.init_state = init_state
        self.receiving_states = receiving_states

    def init_run(self,word):
        result = np.identity(self.num_states)
        reverse_word = word[::-1]
        matrices = [self.dict[letter] for letter in reverse_word]
        for m in matrices:
            result = result @ m

        return result

    def transfer(self,word):
        final_matrix = self.init_run(word)
        for state in self.receiving_states:
            if final_matrix[self.init_state, state] == 1:
                return 1
            else:
                return 0









