#!/usr/bin/env python3

from sqlalchemy import create_engine
from os.path import splitext
import pandas as pd

db_url = 'postgresql+psycopg2://postgres@localhost:15432/postgres'

def read_parquet(filename):
    from fastparquet import ParquetFile as pf
    return pf(filename).to_pandas()

def import_to_sql(df, e, tablename):
    rows, cols = df.shape
    if rows < cols: df = df.transpose()
    df.to_sql(tablename, e)

def import_file_to_sql(filename):
    df = read_parquet(filename) if filename.endswith('.parquet') \
            else pd.read_json(open(filename))
    import_to_sql(df, create_engine(db_url), splitext(filename)[0])

if __name__ == '__main__':
    import sys
    import_file_to_sql(sys.argv[1])

#e.execute('SELECT 1').fetchall()[(1,)]

