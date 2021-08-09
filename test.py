import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import time
api_key = '16V8N6KTWCVUI1J6'

ts = TimeSeries(key=api_key, output_format='pandas')
data_ts, meta_data_ts = ts.get_intraday(symbol='ARKK', interval='1min', outputsize='full')
print(data_ts)



i= 1
while i==1:
    data_ts, meta_data_ts = ts.get_intraday(symbol='ARKK', interval='1min', outputsize='full')
    data_ts.to_excel("output.xlsx")
    time.sleep(60)
p#eriod = 60

#ti = TechIndicators(key=api_key, output_format='pandas')
#data_ti, meta_data_ti = ti.get_sma(symbol='ARKK', interval='1min',
 #                                   time_period=period, series_type='close')

#df1 = data_ti
#df2 = data_ts['4. close'].iloc[period-1::]

#df1.index = df2.index

#total_df = pd.concat([df1, df2], axis=1)
#print(total_df)
#total_df.plot()
#plt.show()
