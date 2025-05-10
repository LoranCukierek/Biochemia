import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as sp
import numpy as np

data = [(0.073, 0.077, 0.095, 0.137, 0.284), (0.084, 0.084, 0.102, 0.185, 0.386), (0.092, 0.095, 0.121, 0.216, 0.296), (0.141, 0.109, 0.136, 0.218, 0.409), (0.116, 0.118, 0.118, 0.249, 0.390), (0.069, 0.065, 0.075, 0.110, 0.191)]
times = [4,8,12,16,20]
solutions = [0.75, 1.5, 3, 6, 12]

data_frame = pd.DataFrame(data)
v = []

for col_id in range(len(data)-1):
    col = data_frame[col_id]
    for i in range(len(col)):
        col[i] -= col[5]
    col = col.loc[0:4]

    slope, intercept, r, p, std_err = sp.linregress(times, col)
    def linregress_func(x):
        return slope*x + intercept
    model = list(map(linregress_func, np.arange(0,25,4)))

    print(slope)
    v.append(1/slope)

    plt.title("wykorzystano substrat o stężeniu:\n" + str(solutions[col_id]) + "mg/ml")
    plt.xlabel("czas [min]")
    plt.ylabel("względna wartość absorbancji")
    plt.grid(True)
    plt.scatter(times, col, color = "skyblue")
    plt.plot(np.arange(0,25,4), model, color = "blue", linestyle = "dashed")
    plt.xticks(np.arange(0,25,4))
    plt.show()


for i in range(len(solutions)):
    solutions[i] = 1/solutions[i]
solutions.reverse()
v.reverse()
plt.scatter(solutions, v)
plt.ylabel("1/v")
plt.xlabel("1/[S]")
plt.show()
