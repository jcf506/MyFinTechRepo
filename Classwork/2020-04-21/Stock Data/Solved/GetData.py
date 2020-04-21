import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:password@localhost:5433/stock_data")

query = "select * from stock_data;"

df = pd.read_sql(query, engine, index_col='stock_data_id')
print(df.head())
