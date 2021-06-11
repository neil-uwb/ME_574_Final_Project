import numpy as np
import pandas as pd
from datetime import datetime
from datetime import timedelta

def data_read_xlsx(data_title):

    data = pd.read_excel(data_title)

    price_index = ''

    date_index = ''

    dates = []

    for i in range(len(data.columns)):

        if 'Prices' in data.columns[i] or 'Price' in data.columns[i]:
        
            price_index = data.columns[i]

        elif 'Dates' in data.columns[i] or 'Date' in data.columns[i]:

            date_index = data.columns[i]

            for j in range(len(data[date_index])):

                dates.append(data[date_index][j])

    return data[price_index],dates,data,price_index

def stats_pull(data,price_idx):

    data['Dates'] = pd.to_datetime(data['Dates'])
    data = data.set_index(data['Dates'])
    data = data.sort_index()

    start_date = data['Dates'][0]
    end_date = data['Dates'][len(data['Dates'])-1]

    count = start_date

    mean = []
    median = []
    date = []

    while True:
            
        mean.append(data[price_idx][str(count.date())].mean())
        median.append(data[price_idx][str(count.date())].median())
        date.append(str(count.date()))
        
        count += timedelta(days = 1)

        if count.date() > end_date.date():

            break

    return mean,median,date    