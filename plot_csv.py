import pandas as pd 
import matplotlib.pyplot as plt
import time

i = 1
while i == 1:
    data = pd.read_csv('output.csv')

    data.iloc[-10:].plot()
    plt.show()
    time.sleep(60)
    plt.close()
