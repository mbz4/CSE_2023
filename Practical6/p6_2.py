import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Problem 2
z0 = np.array([[0],
               [0],
               [0]])

R = 1000
C1 = 10e-9
C2 = 100e-9
L = 0.1

A = np.array([[-1/(R*C1), 0, -1/C1],
              [0, 0, 1/C2],
              [1/L, -1/L, 0]])

B = np.array([[1/(R*C1)],
              [0],
              [0]])

C = np.array([[1, 0, 0],
              [0, 1, 0],
              [1, -1, 0]])

D = 0

sys = ct.ss(A, B, C, D)
time, outputs = ct.step_response(sys)
plt.plot(time, outputs[0][0], label="v1")
plt.plot(time, outputs[1][0], label="v2")
plt.plot(time, outputs[2][0], label="vl-v2")
plt.legend()
plt.show()
