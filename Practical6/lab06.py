import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Problem 1
z0 = np.array([[10000],
               [10],
               [0],
               [0]])

a = 1/100
b = 10/100
c = 1/100
d = 50/100
e = 25/100
f = 1/100

u = np.array([[10],
              [10]])

A = np.array([[-a-b-c, 0, 0, 0],
              [b, -d-e, 0, 0],
              [c, e, -f, 0],
              [a, d, f, 0]])

B = np.array([[1, 0],
              [0, 1],
              [0, 0],
              [0, 0]])

C = np.array([[1, 0, 0, 0],
              [0, 1, 0, 0],
              [0, 0, 1, 0]])

D = np.array([[0, 0],
              [0, 0],
              [0, 0]])

sys = ct.ss(A, B, C, D)
time, outputs = ct.initial_response(sys, T=np.linspace(0, 200, 201), X0=z0)
plt.plot(time, outputs[0], label="Uninfected")
plt.plot(time, outputs[1], label="Infected")
plt.plot(time, outputs[2], label="Immune")
plt.legend()
plt.show()


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
plt.plot(time, outputs[2][0], label="vl")
plt.legend()
plt.show()
