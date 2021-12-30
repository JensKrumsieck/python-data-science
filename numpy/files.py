import numpy as np
np.set_printoptions(suppress=True)

A = np.random.randint(1, 42, size=(3, 3))
print(A)

np.savetxt("A_ignore.txt", A, fmt='%u', delimiter=',')

loadA = np.loadtxt("A_ignore.txt", dtype='u1', delimiter=',')
print(loadA)

print(np.all(loadA == A))  # true
