#!/usr/bin/env python3

from sqlalchemy import create_engine
from os.path import splitext
import pandas as pd

db_url = 'postgresql+psycopg2://postgres@localhost:15432/postgres'

def read_file(fn):
    if fn.endswith('.parquet'):
        from fastparquet import ParquetFile
        return ParquetFile(fn).to_pandas()
    if fn.endswith('.csv'): return pd.read_csv(open(fn), index_col=False)
    return pd.read_json(open(fn))

def import_to_sql(df, e, tablename):
    rows, cols = df.shape
    if rows < cols: df = df.transpose()
    df.to_sql(tablename, e)

def import_file_to_sql(filename):
    e = create_engine(db_url)
    import_to_sql(read_file(filename), e, splitext(filename)[0])

if __name__ == '__main__':
    import sys
    import_file_to_sql(sys.argv[1])

#e.execute('SELECT 1').fetchall()[(1,)]

