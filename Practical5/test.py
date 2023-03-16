#https://pypi.org/project/pytest/
# https://python-control.readthedocs.io/en/0.9.3.post2/control.html
# https://pypi.org/project/control/#history
# https://colab.research.google.com/github/jckantor/CBE30338/blob/master/docs/05.01-Getting-Started-with-Transfer-Functions.ipynb#scrollTo=xSvoZ1FK9itT
# https://www.youtube.com/watch?v=NMpmb0ihoFo&list=PLUMWjy5jgHK3-ca6GP6PL0AgcNGHqn33f&index=4
# https://python-control.readthedocs.io/en/latest/generated/control.sisotool.html

import control
import matplotlib.pyplot as plt
import numpy as np

G = control.tf([8, 15, 2], [7, 1, 3])*control.zpk([-0.0285], [-0.001], 1)
print(G)
#ct.bode_plot(G)
#print(ct.margin(G))
#plt.show()
#T, y = ct.step_response(ct.feedback(35.66/200*G), T = np.linspace(0, 20, 200))
#_, y2 = ct.step_response(H, T = T)
#plt.plot(T, y)
#plt.plot(T, y2)
control.sisotool(G)
plt.show()