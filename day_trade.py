import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import time 
import matplotlib.pyplot as plt 
from matplotlib import style
import matplotlib.animation as animation

api_key = 'HQJMSKJUDBOQB04I'
interval = '1min'
stock = 'INFY'
ts = TimeSeries(key=api_key, output_format = 'pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol = stock, interval = interval, outputsize='full')


period = 15
ti = TechIndicators(key=api_key, output_format = 'pandas')
data_ti, meta_data_ti = ti.get_sma(symbol = stock, interval = interval, time_period = period, series_type='close')

df1 = data_ti
df2 = data_ts['4. close'].iloc[period-1 : :]

df2.index = df1.index
total_df = pd.concat([df1,df2] , axis = 1)
# print(total_df)

# total_df.plot()
# plt.show()
style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
i = 1

while i==1:
    data_ts, meta_data_ts = ts.get_intraday(symbol = stock, interval = interval, outputsize='full')
    data_ts['4. close'].to_csv("output.csv")
    print(data_ts)
    time.sleep(12)


# plot data

