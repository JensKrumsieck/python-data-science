import datetime
import numpy as np
import pandas as pd

dtf = pd.to_datetime([
    "1/1/1970",
    np.datetime64("2011-12-11"),
    datetime.datetime(2012, 1, 2)
])
# D = days, default! 7 einträge!
dtf = pd.date_range("2021-1-2", periods=7, freq='D')
print(dtf)
# DatetimeIndex(['2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
#               '2021-01-06', '2021-01-07', '2021-01-08'],
#              dtype='datetime64[ns]', freq='D')
dtf = pd.date_range("2021-1-2", periods=7, freq='B')  # B = Businessdays
print(dtf)
# DatetimeIndex(['2021-01-04', '2021-01-05', '2021-01-06', '2021-01-07',
#               '2021-01-08', '2021-01-11', '2021-01-12'],
#              dtype='datetime64[ns]', freq='B')

dtf = pd.date_range("2021-1-2", periods=7, freq='5min')
print(dtf)
# DatetimeIndex(['2021-01-02 00:00:00', '2021-01-02 00:05:00',
#               '2021-01-02 00:10:00', '2021-01-02 00:15:00',
#               '2021-01-02 00:20:00', '2021-01-02 00:25:00',
#               '2021-01-02 00:30:00'],

dtf = pd.date_range("13.12.2021", periods=7, freq='D')
print(dtf)
# DatetimeIndex(['2021-12-13', '2021-12-14', '2021-12-15', '2021-12-16',
#               '2021-12-17', '2021-12-18', '2021-12-19'],
#              dtype='datetime64[ns]', freq='D')
print(dtf.strftime("%d.%m.%Y"))
# Index(['13.12.2021', '14.12.2021', '15.12.2021', '16.12.2021', '17.12.2021',
#       '18.12.2021', '19.12.2021'],
#      dtype='object')
print(pd.to_datetime([1625823884]))  # DANGER! UTC nanoseconds!
print(pd.to_datetime([1625823884], unit="s"))
# DatetimeIndex(['2021-07-09 09:44:44'], dtype='datetime64[ns]', freq=None)
