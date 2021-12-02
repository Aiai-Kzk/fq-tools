import numpy as np
import matplotlib.pyplot as plt
import csv
import sys
import seaborn as sns
import scipy
import pandas as pd

plt.figure(figsize = (8.0, 6.0))
plt.subplots_adjust(left=0.14, right=0.98, bottom=0.12, top=0.95)

linestyles = ['-', '--', '-.', ':']
markers = [">", "^", "s", "<", "v", "D"]
legs = ["label1", "label2", "label3"]
colors = ["blue", "red", "green", "orange", "Magenta", "orange", "Magenta"]
labels = [""]

labels = [""] * len(sys.argv)
MARKEVERY = 10
MARKSIZE = 15

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20

rssi = []
tmp = []
mcs = list(range(0, 8))

df_per = pd.read_csv('per.csv')
columns = df_per.columns

for i in range(len(columns)):

    plt.errorbar(mcs, df_per[columns[i]], label = columns[i], marker = markers[i], color = colors[i], markeredgewidth = 2, linewidth = 0, linestyle = "--", dashes = (i + 1, i + 1), markerfacecolor = 'None', ms = MARKSIZE)

# plt.rcParams['xtick.direction'] = 'in'
# plt.rcParams['ytick.direction'] = 'in'
plt.legend(frameon = False, ncol = 1, loc = 'upper left', fontsize = 20)
plt.grid()

plt.xlabel("modualtion coding schemes (MCS)")
plt.ylabel("packet error rate (PER)")

plt.yscale("log")

#plt.xlim(-35, -15)
plt.ylim(0, 1)
#plt.yticks(np.arange(0, 1.1, 1/5))
plt.xticks(mcs)

# #

plt.savefig("per.png")   
plt.savefig("per.eps")   
plt.show()
# #plt.savefig("ex_pa.eps")  