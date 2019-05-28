import numpy as np

class StateMachine():

    def __init__(self, dict, num_states, init_state, receiving_states):
        self.dict = dict
        self.num_states = num_states
        self.init_state = init_state
        self.receiving_states = receiving_states

    def prep_run(self,word): #matrix list for word
        matrices = [self.dict[letter] for letter in word]
        return matrices

    def prep_machine(self,matrices): #flip matrix order for math..
        return matrices[::-1]

    def run_machine(self,matrices): #multiply matrices and get final state
        result = np.identity(self.num_states)
        matrices = self.prep_machine(matrices)
        for m in matrices:
            result = result @ m
        final_state = result @ self.init_state
        return final_state

    def check_final_state(self,final_state): #check if final state is accepted
        accept_prob = int(abs(np.dot(np.transpose(self.receiving_states), final_state)) ** 2)
        return accept_prob

    def transfer(self,word):
        matrices = self.prep_run(word)
        matrices = self.prep_machine(matrices)
        final_state = self.run_machine(matrices)
        prob = self.check_final_state(final_state)
        return prob

    # def transfer(self,word):
    #     final_matrix = self.init_run(word)
    #     final_state = final_matrix @ self.init_state
    #     a = np.transpose(self.receiving_states)
    #     accept_prob = int(abs(np.dot(np.transpose(self.receiving_states),final_state))**2)
    #
    #     return accept_prob









