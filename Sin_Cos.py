import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

x = np.arange(0,7*np.pi,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y, "bo", x , z, "gx")
plt.axis([0,25, -1, 1])
plt.ylabel("sin(x) and cos(x)")
plt.xlabel("x values from 0 to 7pi")
plt.title("Plot of sin and cos from 0 to 7pi")
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
