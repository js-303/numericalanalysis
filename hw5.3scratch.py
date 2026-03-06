import numpy as np
import matplotlib.pyplot as plt

S = [1, 2, 3]

def m_process(a, start_state, n):
    p = np.array([[1-a, a,   0  ],
                  [a,   0,   1-a],
                  [0,   1-a, a  ]])
    
    state_index = S.index(start_state)
    state_sequence = [start_state]

    for _ in range(n):
        state_index = np.random.choice(len(S), p=p[state_index])
        state_sequence.append(S[state_index])

    return state_sequence

num_chains = 10**5
n_steps = 10**2
all_chains = []
for _ in range(num_chains):
    a = np.random.uniform(0, 1)
    all_chains.append(m_process(a, 1, n_steps))

all_chains = np.array(all_chains)  # shape: (num_chains, n_steps + 1)

# f_n: fraction in state 1 at each time step
f_n = [np.mean(all_chains[:, n] == 1) for n in range(1, n_steps + 1)]

plt.plot(range(1, n_steps + 1), f_n, label='$f_n$ (simulated)')
plt.plot(range(1, n_steps + 1), np.full(n_steps, 1/3), linestyle='--', label='$q_n = 1/3$ (theoretical)')
plt.xlabel('n')
plt.ylabel('Fraction in state 1')
plt.legend()
plt.show()