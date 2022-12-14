import matplotlib.pyplot as plt
import numpy as np


def draw_plot(xy_datas, colors):
    fig, ax = plt.subplots()
    for i, line in enumerate(xy_datas):
        ax.plot(line[0], line[1], color=colors[i])

    ax.set_ylim(-5, 10)
    ax.set_xlim(-5, 10)
    ax.set_yticks(np.arange(-5, 10, 1))
    ax.set_xticks(np.arange(-5, 10, 1))
    ax.grid(color='grey', linewidth=0.5, linestyle='-')
    plt.show()
