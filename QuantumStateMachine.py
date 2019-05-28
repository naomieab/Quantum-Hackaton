# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:37:11 2019

@author: Naomie Abecassis
"""


import numpy as np
from qiskit import *
from qiskit import BasicAer

from state_machine import StateMachine


class QuantumStateMachine(StateMachine) :

    def prep_machine(self,matrices): #flip matrix order for math..
        q = QuantumRegister(2, 'q')
        # TODO set start state with unitary operator
        circ = QuantumCircuit(q)
        circ.h(q[1])
        for matrix in matrices:
            circ.unitary(matrix, q)
        circ.draw()
        return circ

    def run_machine(self, circ): #multiply matrices and get final state
        backend = BasicAer.get_backend('statevector_simulator')
        job = execute(circ, backend)
        result = job.result()
        outputstate = result.get_statevector(circ, decimals=3)
        return outputstate

    def check_final_state(self,final_state): #check if final state is accepted
        accept_prob = float(abs(np.dot(final_state, self.receiving_states)) ** 2)
        return accept_prob



