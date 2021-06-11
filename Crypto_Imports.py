import pandas as pd
from numba import cuda
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def crypto_pull(crypto_loc):
    data = pd.read_csv(crypto_loc)

    del data[data.columns[2]]
    del data[data.columns[3]]
    del data[data.columns[4]]
    del data[data.columns[5]]

    data['date'] = pd.to_datetime(data['date'])
    data = data.set_index(data['date'])
    data = data.sort_index()

    return data

def crypto_date_set(gpu_dates_array,crypto_data):

    

    crypto_value = []

    for i in range(len(crypto_data['4a. close (USD)'])):

        if str((crypto_data['date'][i]).date()) in gpu_dates_array:

            crypto_value.append(crypto_data['4a. close (USD)'][i])

    return crypto_value

def numpy_conv(mean,median,crypto_values):
    return np.array(mean),np.array(median),np.array(crypto_values)

@cuda.jit()
def crypto_gpu_compare(mean,median,crypto_values,out1,out2):

    for i in range(len(mean)):
        out1[i] = mean[i]/crypto_values[i]
        out2[i] = median[i]/crypto_values[i]

def crypto_gpu_graph_generator(mean,median,dates,name):

    mean = np.array(mean)
    median = np.array(median)
    dates = [datetime.strptime(x,'%Y-%m-%d') for x in dates]

    plt.plot(dates,mean,label = 'Mean GPU Price/BTC')
    plt.plot(dates,median, label = 'Median GPU Price/BTC')
    plt.legend()
    plt.xticks(rotation = 30)
    plt.xlabel('Date')
    plt.ylabel('GPU Price/BTC (USD)')
    plt.title('RTX ' + name + ' vs BTC Price Comparison')
    plt.show()

@cuda.jit()
def gpu_diff(gpu1, gpu2,out):
    thread_position = cuda.grid(1)
    temp = gpu1[thread_position]-gpu2[thread_position]
    out[thread_position] += (temp**2)**.5

def gpu_diff_graph(name1,name2,diff1,diff2,dates):
    dates = [datetime.strptime(x,'%Y-%m-%d') for x in dates]

    plt.plot(dates,diff1,label = 'Mean Difference between RTX ' + str(name1) + ' and RTX ' + str(name2))
    plt.plot(dates,diff2,label = 'Median Difference between RTX ' + str(name1) + ' and RTX ' + str(name2))
    plt.xticks(rotation = 30)
    plt.legend()
    plt.xlabel('Date')
    plt.ylabel('GPU Price Difference (USD)')
    plt.title('RTX ' + str(name1) + ' vs RTX ' + str(name2) + ' Price Difference')
    plt.show()