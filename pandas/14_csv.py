from datetime import date
import numpy as np
import pandas as pd

dateframe = pd.DataFrame(
    np.random.randn(100, 2),
    columns=[1, 2],
    index=pd.date_range("20211212", periods=100, freq="5min")
)
print(dateframe)

dateframe.to_csv("data_ignore.csv", sep=";", index_label="time")

# squeeze=True -> make series
incoming = pd.read_csv("data_ignore.csv", sep=";", index_col=0, parse_dates=True)
print(incoming)
