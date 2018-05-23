#!/usr/bin/env python3

from sqlalchemy import create_engine
from os.path import splitext
import pandas as pd

db_url = 'postgresql+psycopg2://postgres@localhost:15432/postgres'

def import_json_to_sql(filename):
    e = create_engine(db_url)
    tablename = splitext(filename)[0]
    df = pd.read_json(open(filename))
    rows, cols = df.shape
    if rows < cols: df = df.transpose()
    df.to_sql(tablename, e)

if __name__ == '__main__':
    import sys
    import_json_to_sql(sys.argv[1])

#e.execute('SELECT 1').fetchall()[(1,)]

