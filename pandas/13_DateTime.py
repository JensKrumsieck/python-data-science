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

dateframe = pd.DataFrame(
    np.random.randn(100000, 2),
    columns=["Player 1", "Player 2"],
    index=pd.date_range("20211213", periods=100000,
                        freq="5min", tz="Europe/Berlin")
)
# january 2022 all data!
print(dateframe["2022-01-01 00:00:00+01:00":"2022-02-02 00:00:00+01:00"])
print(dateframe.loc["2022"])  # get all 2022

print(dateframe.loc["2022-01-01 00:00:00+01:00"])  # get new year
# Player 1   -0.161197
# Player 2   -0.921572
# Name: 2022-01-01 00:00:00+01:00, dtype: float64
#print(dateframe.truncate(before="2022", after="2023"))
print("------------------------------------------------------")
delta = pd.Timedelta("1 day 1h")
print(delta)  # 1 days 01:00:00

print(pd.to_datetime("2021") + delta)
# 2021-01-02 01:00:00

print(pd.Timestamp.now())  # 2022-01-02 19:59:58.949053

df = pd.DataFrame(
    pd.date_range("20220101", periods=10, freq="5h"),
    columns=["time"]
)
print(df)
#                 time
# 0 2022-01-01 00:00:00
# 1 2022-01-01 05:00:00
# 2 2022-01-01 10:00:00
# 3 2022-01-01 15:00:00
# 4 2022-01-01 20:00:00
# 5 2022-01-02 01:00:00
# 6 2022-01-02 06:00:00
# 7 2022-01-02 11:00:00
# 8 2022-01-02 16:00:00
# 9 2022-01-02 21:00:00

print(df.shift())  # move down list
#                 time
# 0                 NaT
# 1 2022-01-01 00:00:00
# 2 2022-01-01 05:00:00
# 3 2022-01-01 10:00:00
# 4 2022-01-01 15:00:00
# 5 2022-01-01 20:00:00
# 6 2022-01-02 01:00:00
# 7 2022-01-02 06:00:00
# 8 2022-01-02 11:00:00
# 9 2022-01-02 16:00:00

print(df.shift().dropna())  # move down list and drop NaT
#  time
# 1 2022-01-01 00:00:00
# 2 2022-01-01 05:00:00
# 3 2022-01-01 10:00:00
# 4 2022-01-01 15:00:00
# 5 2022-01-01 20:00:00
# 6 2022-01-02 01:00:00
# 7 2022-01-02 06:00:00
# 8 2022-01-02 11:00:00
# 9 2022-01-02 16:00:00

print(df + delta)  # add timespan
#                 time
# 0 2022-01-02 01:00:00
# 1 2022-01-02 06:00:00
# 2 2022-01-02 11:00:00
# 3 2022-01-02 16:00:00
# 4 2022-01-02 21:00:00
# 5 2022-01-03 02:00:00
# 6 2022-01-03 07:00:00
# 7 2022-01-03 12:00:00
# 8 2022-01-03 17:00:00
# 9 2022-01-03 22:00:00
