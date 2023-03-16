import control
import matplotlib.pyplot as plt
import numpy as np

G = control.tf([8, 15, 2], [7, 1, 3])*control.zpk([-0.0285], [-0.001], 1)
print(G)
# ~ ct.bode_plot(G)
# ~ print(ct.margin(G))
# ~ plt.show()
# ~ T, y = ct.step_response(ct.feedback(35.66/200*G), T = np.linspace(0, 20, 200))
# ~ _, y2 = ct.step_response(H, T = T)
# ~ plt.plot(T, y)
# ~ plt.plot(T, y2)
control.sisotool(G)
plt.show()