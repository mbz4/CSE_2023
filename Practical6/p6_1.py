import control as ct
import numpy as np
import matplotlib.pyplot as plt

# Problem 1
z0 = np.array([[10000],
               [10],
               [0],
               [0]])

a = 1/100 # natural causes
b = 10/100 # infecgted rate
c = 1/100 # immunized rate
d = 50/100 # inf dead
e = 25/100 # inf cured
f = 1/100 # immune death rate

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
              [0, 0, 1, 0],
              [0, 0, 0, 1]])

D = np.array([[0, 0],
              [0, 0],
              [0, 0],
              [0, 0]])

sys = ct.ss(A, B, C, D)
print(sys)
# https://python-control.readthedocs.io/en/0.9.3.post2/generated/control.input_output_response.html#control.input_output_response
time, outputs = ct.input_output_response(sys, U=[10, 10], T=np.linspace(0, 200, 201), X0=z0)
plt.plot(time, outputs[0], label="Uninfected")
plt.plot(time, outputs[1], label="Infected")
plt.plot(time, outputs[2], label="Immune")
plt.plot(time, outputs[3], label="Deceased")
plt.legend()
plt.show()
