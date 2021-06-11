#!/usr/bin/env python3
import ujson
import requests
import logging
import typing
import bpdb

from typing import Optional
import pandas as pd


def export_as_dataframe():
    url = f'http://localhost:8428/api/v1/export?match[]="{{name!=""}}"'
    logging.info("Got data from" + url)
    df = pd.read_json(url, lines=True)
    return df
    # metricNames = [i['__name__'].replace('aggTrade_', '') for i in df['metric']] + ['timestamp']
    # metricVals = [flatten(df['values'][0]), flatten(df['values'][1]), flatten(df['values'][2]), flatten(df['values'][3]), flatten(df['timestamps'][0])]
    # bpdb.set_trace()
    d = {x:y for x,y in zip(metricNames, metricVals)}
    df = pd.DataFrame(d)



if __name__ == "__main__":
    df = export_as_dataframe()
