# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:37:11 2019

@author: Naomie Abecassis
"""


import numpy as np
from qiskit import *
from qiskit import BasicAer



class QuantumStateMachine : 
    def __init__(self):
        pass
    
    def circuit(self, word):
        matrix_array = init_run(word)
        q = QuantumRegister(2, 'q')
        circ = QuantumCircuit(q)
        for matrix_product in matrix_array:
            for matrix in matrix_product:
                circ.unitary(matrix)
        circ.draw()
        backend = BasicAer.get_backend('statevector_simulator')
        job = execute(circ, backend)
        result = job.result()
        outputstate = result.get_statevector(circ, decimals=3)
        print(outputstate)
        pass
    
#a = np.matrix('1 0; 0 1')

matrix = [np.array([[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]), 
          np.array([[0, 0, 0, 1],[0, 0, 1, 0],[0, 1, 0, 0],[1, 0, 0, 0]])]     
q = QuantumRegister(2, 'q')
circ = QuantumCircuit(q)
for matric in matrix:
   circ.unitary(matric, q)
circ.draw()
