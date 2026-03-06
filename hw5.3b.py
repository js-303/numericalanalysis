import numpy as np
import sympy as sp

a = sp.symbols('a', positive=True)
S = [1,2,3]
p = sp.Matrix([[1-a,a,0],
              [a,0,1-a],
              [0,1-a,a]])

p_T = p.T

evals = p.eigenvals()
evecs = p.eigenvects()

n = 10**3

def m_process(p, start_state, n):
    state_index = S.index(start_state)
    state_sequence = [start_state]

    for _ in range(n):
        state_index = np.random.choice(range(len(S)), p=p[state_index])
        state_sequence.append(S[state_index])

    return state_sequence

process = m_process(p, 1, n)

print(process)
print(p)
print(p_T)

print("Evals: ", evals)
print("Evecs: ", evecs)
