import matplotlib.pyplot as plt
import numpy as np


class Drone:

    def place_drone(self,x, y):
        x = np.array(x)
        y = np.array(y)
        plt.plot(x, y)
        plt.xlim(0, 12)
        plt.ylim(0, 12)
        plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        plt.grid()
        plt.show()

    def move_north(self,x_cor,y_cor):
        next_y_cor = y_cor[-1] + 1
        y_cor.append(next_y_cor)
        x_cor.append(x_cor[-1])


    def move_south(self,x_cor,y_cor):
        next_y_cor = y_cor[-1] - 1
        y_cor.append(next_y_cor)
        x_cor.append(x_cor[-1])


    def move_east(self,x_cor,y_cor):
        next_x_cor = x_cor[-1] + 1
        x_cor.append(next_x_cor)
        y_cor.append(y_cor[-1])


    def move_west(self,x_cor,y_cor):
        next_x_cor = x_cor[-1] - 1
        x_cor.append(next_x_cor)
        y_cor.append(y_cor[-1])
