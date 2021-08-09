import requests
import json
import pandas as pd
import smtplib
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
import time
import pywhatkit
api_key = '16V8N6KTWCVUI1J6'


def sendemail(message):
    email = 'coffeegarden123@gmail.com'
    password = 'jjaaccoobb123'

    header = 'From: %s\n' % (email)
    header += 'To: %s\n' % (email)
    header += 'Cc: %s\n' % (email)
    header += 'Subject: %s\n\n' % ('SMA Alert')
    message = header + message

    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(email, password)
    problems = server.sendmail(email, email, message)
    server.quit()
    return problems
    
    
    
ts = TimeSeries(key=api_key, output_format='pandas')
#data_ts, meta_data_ts = ts.get_intraday(symbol='ARKK', interval='1min', outputsize='full')
#print(data_ts)
i= 1
while i==1:
    data_ts, meta_data_ts = ts.get_intraday(symbol ='ARKK', interval ='1min', outputsize ='full')
  
#  data_ts.to_excel("output.xlsx")
 #   time.sleep(60)
    close_data = data_ts['4. close']
    percentage_change = close_data.pct_change()
    last_change = percentage_change[-1]
 
    print(close_data.iloc[:10] ) # print the last 10 data
    #print (percentage_change.iloc[:10])
    print("The last % change is= ", last_change)
    if abs(last_change) > 0.0001:
    #pywhatkit.sendwhatmsg('+16475181721','alerts for stock',18,50)
       sendemail("Last change of stock price is greater than 0.0001. please take a look at the stock app")
       print ('mail sent')
    
    
    
    
    time.sleep(60) 


