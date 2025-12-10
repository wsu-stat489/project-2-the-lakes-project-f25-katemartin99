import polars as pl
from column_data import cols_to_keep

column_schema = {col: pl.String for col in cols_to_keep}
