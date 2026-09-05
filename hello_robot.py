import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel("time")
plt.ylabel("position")
plt.title("Robot Signal")
plt.show()