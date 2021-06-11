import pandas as pd
import numpy as np
#import time
from random import randrange
from datetime import timedelta
from datetime import datetime

#from stackexchange
def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2020 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('6/10/2021 4:50 AM', '%m/%d/%Y %I:%M %p')
def data_generator(size,low,high,name):
    rtx3090_price = np.random.randint(low,high,size)
    dates = []
    for i in range(0,size):
        dates.append(random_date(d1,d2))

    #assuming this is a 3090
    data = pd.DataFrame([dates,rtx3090_price],index = ['Dates','RTX ' + str(name) +' Prices'])
    data.T.to_excel(str(name)+'.xlsx', sheet_name = 'Sheet1')
    #data.T.to_csv('test_gpu_price_data.csv')

    #return 'RTX ' + str(name) +' Prices'

