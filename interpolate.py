# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:49:46 2019

@author: APH8KOR
"""

#import pandas as pd
#import matplotlib.pyplot as plt
#from datetime import datetime
#from pandas import to_datetime,date_range
#import sqlite3
#from dateutil.parser import parse 
#
#file_name='Virginia_Oktober.xlsx'
#
#db_1_path = "logs1.db"
#
#df_chamber=pd.read_excel(file_name,'Tabelle1',parse_dates=['time'], index_col='time'))
#df_chamber["time"]=pd.to_datetime(df_chamber["time"])
#df_chamber=df_chamber.set_index(['time'])
#
#conn = sqlite3.connect(db_1_path)
#df_pi=pd.read_sql_query("SELECT * FROM Raspberry3", conn)
#df_pi["time"]=pd.to_datetime(df_pi["time"])
#df_pi=df_pi.set_index(['time'])
#
#print(df_chamber.sub(df_pi.rename(columns={'temperature': 'temp'}), fill_value=0))
##print(df_chamber)

import matplotlib.pyplot as plt
from pandas import read_csv
from pandas import to_datetime,date_range,DataFrame
import numpy as np
import pandas as pd
import sqlite3

file_name='Virginia_Oktober.xlsx'

db_1_path = "logs1.db"

# load dataset
startTime=to_datetime('23.10.2019 15:59')
endTime=to_datetime('24.10.2019 00:59')

newIndex = to_datetime(date_range(startTime, endTime, freq='30s'), )
newIndex = pd.to_datetime(newIndex)
newIndex = newIndex.strftime('%Y-%m-%d %H:%M')
conn = sqlite3.connect(db_1_path)
series = pd.read_sql_query("SELECT * FROM Raspberry3", conn)
series['time'] = pd.to_datetime(series['time'])
series['time'] = series['time'].dt.strftime('%Y-%m-%d %H:%M')
new = pd.Series()
for t in newIndex:
  li = series.loc[series['time']==t]
  mn = li.loc[:,'temperature'].mean()
  new.set_value(t,mn)



