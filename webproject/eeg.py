import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    # /Users/shrutishah/Library/CloudStorage/GoogleDrive-1795898@fcpsschools.net/Shared drives/mindMusic/webproject/data.csv
    
    data = pd.read_csv('G:\Shared drives\mindMusic\webproject\data.csv')
    x = data['time']
    y1 = data['engagement']
    y2 = data['focus']
    y3 = data['excitement']
    y4 = data['stress']
    y5 = data['relaxation']
    y6 = data['interest']

    plt.cla()

    plt.plot(x, y1, label='engagement')
    plt.plot(x, y2, label='focus')
    plt.plot(x,y3, label="excitement")
    plt.plot(x,y4,label='stress')
    plt.plot(x,y5, label = 'relaxation')
    plt.plot(x,y6, label='interest')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10000)

plt.tight_layout()
plt.show()