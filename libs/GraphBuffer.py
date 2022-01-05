import math
import numpy as np
import matplotlib.pyplot as plt


class GraphBuffer:
    # data_to_plot[0,i] = t
    # data_to_plot[1,i] = Delta_t
    # data_to_plot[2,i] = A_xt
    # data_to_plot[3,i] = A_yt
    # data_to_plot[4,i] = A_x
    # data_to_plot[5,i] = A_y
    # data_to_plot[6,i] = B_x
    # data_to_plot[7,i] = B_y
    # data_to_plot[8,i] = f

    def __init__(self, N):
        self.data_to_plot = np.empty([9,N], dtype = np.float32)
        self.last_used = 0
        self.Ndata = N

    def updateGraphBuffer(self, new_data):
        assert(self.last_used < self.Ndata)
        for j in range(0,9):
            self.data_to_plot[j,self.last_used] = new_data[j]
        self.last_used += 1

    def plotGraphBuffer(self):
        plt.rcParams['figure.figsize'] = [10, 8]
        fig, (ax1, ax2) = plt.subplots(2)

        ax1.set_title('posizioni')
        ax1.set_xlabel('$\it{x}$ [m]')
        ax1.set_ylabel('$\it{y}$ [m]')
        ax1.plot(self.data_to_plot[2], self.data_to_plot[3])
        ax1.plot(self.data_to_plot[6], self.data_to_plot[7])
    
        ax2.set_title('frequenza')
        ax2.set_xlabel('$\it{t}$ [s]')
        ax2.set_ylabel('$\it{f}$ [Hz]')
        ax2.plot(self.data_to_plot[0], self.data_to_plot[8])

        ax1.grid(visible=True, which='major', color='#666666', linestyle='-')
        ax2.grid(visible=True, which='major', color='#666666', linestyle='-')
        
        fig.tight_layout()
        plt.show(block = False)
