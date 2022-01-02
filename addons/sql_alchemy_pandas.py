import sqlalchemy
import pandas as pd
import numpy as np
from sqlalchemy import Integer

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:@localhost:3306/pandas_data")
conn = engine.connect()

df = pd.DataFrame(np.random.randint(0, 100, (100, 3)))
df.rename({0: "A", 1: "B", 2: "C"}, axis=1, inplace=True)
print(df)

table_name = "simple"

df.to_sql(table_name,
          engine,
          if_exists="replace",
          index=False,
          chunksize=500,
          dtype={
              "A": Integer,
              "B": Integer,
              "C": Integer
          }
          )
# -> DROP TABLE IF EXISTS simple; CREATE TABLE simple ...
