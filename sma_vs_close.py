import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = '16V8N6KTWCVUI1J6'

ts = TimeSeries(key=api_key, output_format='pandas') ## pass on the api token to start recieving data, use pandas to organize your data 
data_ts, meta_data_ts = ts.get_intraday(symbol='ARKK', interval='1min', outputsize='full') #data_ ts and meta_data gets the stock price for ARKK stock every 1  min 

period = 60

ti = TechIndicators(key=api_key, output_format='pandas') # time indicator has less data than time series and it's more specific on times and series type
data_ti, meta_data_ti = ti.get_sma(symbol='ARKK', interval='1min',
                                    time_period=period, series_type='close')

df1 = data_ti
df2 = data_ts['4. close'].iloc[59::]# the 4 columns of time series data is the close value and becuz we don't want other series type

#df1.index = df2.index # iloc 59:: is to remove the first 59 data to matach the data/indes of df1

total_df = pd.concat([df1, df2], axis=1) ## display two types of values from intraday and SMA 
print(total_df)

total_df.plot()
plt.show()  # plot the graph 
