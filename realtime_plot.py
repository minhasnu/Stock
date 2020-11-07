# import pandas as pd
# from alpha_vantage.timeseries import TimeSeries
# from alpha_vantage.techindicators import TechIndicators
# import matplotlib.pyplot as plt 

# api_key = 'HQJMSKJUDBOQB04I'
# interval = '1min'
# stock = 'INFY'

# ts = TimeSeries(key=api_key, output_format = 'pandas')
# ti = TechIndicators(key=api_key, output_format = 'pandas')
# period = 100
# i = 1

# while i==1:
#     data_ti, meta_data_ti = ti.get_sma(symbol = stock, interval = interval, time_period = period, series_type='close')
#     data_ts, meta_data_ts = ts.get_intraday(symbol = stock, interval = interval, outputsize='full')
#     df1 = data_ti
#     df2 = data_ts['4. close'].iloc[period-1 : :]
#     df2.index = df1.index
#     total_df = pd.concat([df1,df2] , axis = 1)
#     print(total_df)
#     total_df.iloc[-300:].plot()
#     # # plt.show()
#     # time.sleep(1)
#     # plt.close()
#     # time.sleep(4)
 
   
import pandas as pd
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('output.csv','r').read()
    
    lines = data.split('\n')

    lines = lines[-100:]
    
    #print(lines)
    # print('\n')
    xs = []
    ys = []
    # print(lines)
    for line in lines:
        # print(line)
        if(len(line) > 1):
            x, y = line.split(',')           
            xs.append(x)
            ys.append(y)
            # print(x,y)
    ax1.clear()
    ax1.plot(xs, ys)
ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
