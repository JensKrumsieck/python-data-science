from sqlalchemy import Integer
import numpy as np
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine(
    "mysql+pymysql://root:@localhost:3306/pandas_data")
conn = engine.connect()
res = conn.execute("SELECT * FROM simple").fetchall()
print(res)

table_name = "simple"
table_df = pd.read_sql_table(
    table_name,
    con=engine,
    index_col=False,
    columns=[
        "A",
        "C"
    ])
print(table_df)
