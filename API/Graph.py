import random
from Delay import ping_delay
import time

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib import animation



class Array:

    def __init__(self):

        self.array = [0, 0, 0, 0, 0, 0]

    def update_array(self, new_value):

        del self.array[0]
        self.array.append(new_value)

    def init(self):
        return [self.e1]

    def animate(self, i):
        self.update_array(random.random())
        self.e1.set_ydata(self.array)
        return [self.e1]

    def plot(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, aspect='equal')
        self.e1 = Line2D(xdata=[0, 1, 2, 3, 4, 5], ydata=self.array, linewidth=0.5, animated=True)
        self.ax.add_line(self.e1)

        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init, interval=1000, blit=True)
        plt.xlim([0, 5])
        plt.show()

array = Array()

array.plot()
