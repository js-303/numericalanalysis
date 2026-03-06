import numpy as np
import matplotlib.pyplot as plt

K = 0.1
a = 0.04
b = 0.16

S = [1,2,3,4,5]
p = np.zeros((5,5))

for n in S:
    if n+1 <= S[-1]:
        p_n = K*np.exp(a*n)
        p[n-1][n] = p_n
    if n-1 >= S[0]:
        q_n = K*np.exp(b*(n-1))
        p[n-1][n-2] = q_n
    if n-1 >= S[0] and n+1 <= S[-1]:
        p[n-1][n-1] = 1 - p[n-1][n] - p[n-1][n-2]
    elif n-1 < S[0]:
        p[n-1][n-1] = 1 - p[n-1][n]
    elif n+1 > S[-1]:
        p[n-1][n-1] = 1 - p[n-1][n-2]

    
print(p)


n = 10**6

def m_process(p, start_state, n):
    state_index = S.index(start_state)
    state_sequence = [start_state]

    for _ in range(n):
        state_index = np.random.choice(range(len(S)), p=p[state_index])
        state_sequence.append(S[state_index])

    return state_sequence

process = m_process(p, 4, n)

counts = {}
ratios = {}
for s in S:
    counts[s] = 0
for state in process:
    counts[state] += 1
for s in S:
    ratios[s] = counts[s] / n

print(f"counts: {counts}")
print(f"ratios: {ratios}")

pi_1 = 0.29651
db_sd = [pi_1, pi_1*np.exp(-0.12), pi_1*np.exp(-0.36), pi_1*np.exp(-0.72), pi_1*np.exp(-1.2)]

P_T = p.T
evals, evecs = np.linalg.eig(P_T)
for i in range(len(evals)):
    if np.isclose(evals[i], 1, atol=1e-13):
        print("eval:", i)
        print("evec:", evecs[:, i])
        selected_evec = evecs[:, i]
        evec_sd = selected_evec/np.linalg.norm(selected_evec, ord=1)

fig, (ax1,ax2,ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8,6))
ax1.bar(S, ratios.values(), color='blue', alpha=0.5)
ax1.set_title("Fraction of Time \n Spent in Each State")
ax1.set_xlabel("State")
ax1.set_ylabel("Fraction of Time")
ax1.set_xticks(S)  
ax2.bar(S, evec_sd, color='green', alpha=0.5)
ax2.set_title("Stationary Distribution \n from Eigenvector")
ax2.set_xlabel("State")
ax2.set_ylabel("Probability")
ax2.set_xticks(S)
ax3.bar(S, db_sd, color='orange', alpha=0.5)
ax3.set_title("Stationary Distribution \nfrom Detailed Balance")
ax3.set_xlabel("State")
ax3.set_ylabel("Probability")
ax3.set_xticks(S)
plt.tight_layout()
plt.show()

