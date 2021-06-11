from data_read import data_read_xlsx,stats_pull
from Crypto_Imports import *
from Project_Data_Generator import data_generator
from crypto_api import crypto_data_gen

def gpu_3060():
    gpu_type = 3060

    print('Name Generatred:', gpu_type)

    #name = data_generator(10000,600,2000,gpu_type)
    data_generator(10000,600,2000,gpu_type)

    print('Data Generated for RTX', gpu_type)

    data_set = str(gpu_type) + '.xlsx'

    print('Data Imported for RTX', gpu_type)

    #data is a returned as pandas data type that needs to be converted into a numpy array if it is to be used in CUDA based code

    #look to remove prices and data from data_read_xlsx

    prices,dates,data,price_idx = data_read_xlsx(data_set)
    #print(data)
    btc_prices = crypto_pull('BTC.csv')
    #print(btc_prices)
    mean,median,gpu_dates_array = stats_pull(data,price_idx)
    crypto_value = crypto_date_set(gpu_dates_array,btc_prices)
    mean,median,crypto_value = numpy_conv(mean,median,crypto_value)

    #mean/crypto
    out1 = np.zeros(len(mean))
    #median/crypto
    out2 = np.zeros(len(mean))

    n = mean.size
    TPB = 32
    block = (n+TPB-1)//TPB
    crypto_gpu_compare[block,TPB](mean,median,crypto_value,out1,out2)


    #mean, median, dates, name
    crypto_gpu_graph_generator(out1,out2, gpu_dates_array, str(gpu_type))

    print('Function Completed:',gpu_type)

    return mean, median, gpu_type, gpu_dates_array

def gpu_3070():
    gpu_type = 3070

    print('Name Generatred:', gpu_type)

    #name = data_generator(10000,800,3000,gpu_type)
    data_generator(10000,800,3000,gpu_type)

    print('Data Generated for RTX', gpu_type)

    data_set = str(gpu_type) + '.xlsx'

    print('Data Imported for RTX', gpu_type)

    #data is a returned as pandas data type that needs to be converted into a numpy array if it is to be used in CUDA based code

    #look to remove prices and data from data_read_xlsx

    prices,dates,data,price_idx = data_read_xlsx(data_set)
    #print(data)
    btc_prices = crypto_pull('BTC.csv')
    #print(btc_prices)
    mean,median,gpu_dates_array = stats_pull(data,price_idx)
    crypto_value = crypto_date_set(gpu_dates_array,btc_prices)
    mean,median,crypto_value = numpy_conv(mean,median,crypto_value)

    out1 = np.zeros(len(mean))
    out2 = np.zeros(len(mean))

    n = mean.size
    TPB = 32
    block = (n+TPB-1)//TPB
    crypto_gpu_compare[block,TPB](mean,median,crypto_value,out1,out2)

    #mean, median, dates, name
    crypto_gpu_graph_generator(out1,out2, gpu_dates_array, str(gpu_type))

    print('Function Completed:',gpu_type)

    return mean, median, gpu_type

def gpu_3080():
    gpu_type = 3080

    print('Name Generatred:', gpu_type)

    #name = data_generator(10000,1000,4500,gpu_type)
    data_generator(10000,1000,4500,gpu_type)

    print('Data Generated for RTX', gpu_type)

    data_set = str(gpu_type) + '.xlsx'

    print('Data Imported for RTX', gpu_type)

    #data is a returned as pandas data type that needs to be converted into a numpy array if it is to be used in CUDA based code

    #look to remove prices and data from data_read_xlsx

    prices,dates,data,price_idx = data_read_xlsx(data_set)
    #print(data)
    btc_prices = crypto_pull('BTC.csv')
    #print(btc_prices)
    mean,median,gpu_dates_array = stats_pull(data,price_idx)
    crypto_value = crypto_date_set(gpu_dates_array,btc_prices)
    mean,median,crypto_value = numpy_conv(mean,median,crypto_value)

    out1 = np.zeros(len(mean))
    out2 = np.zeros(len(mean))

    n = mean.size
    TPB = 32
    block = (n+TPB-1)//TPB
    crypto_gpu_compare[block,TPB](mean,median,crypto_value,out1,out2)

    #mean, median, dates, name
    crypto_gpu_graph_generator(out1, out2, gpu_dates_array, str(gpu_type))

    print('Function Completed:',gpu_type)

    return mean, median, gpu_type

def gpu_3090():
    gpu_type = 3090

    print('Name Generatred:', gpu_type)

    #name = data_generator(10000,2000,6000,gpu_type)
    data_generator(10000,2000,6000,gpu_type)

    print('Data Generated for RTX', gpu_type)

    data_set = str(gpu_type) + '.xlsx'

    print('Data Imported for RTX', gpu_type)

    #data is a returned as pandas data type that needs to be converted into a numpy array if it is to be used in CUDA based code

    #look to remove prices and data from data_read_xlsx

    prices,dates,data,price_idx = data_read_xlsx(data_set)
    #print(data)
    btc_prices = crypto_pull('BTC.csv')
    #print(btc_prices)
    mean,median,gpu_dates_array = stats_pull(data,price_idx)
    crypto_value = crypto_date_set(gpu_dates_array,btc_prices)
    mean,median,crypto_value = numpy_conv(mean,median,crypto_value)

    out1 = np.zeros(len(mean))
    out2 = np.zeros(len(mean))

    n = mean.size
    TPB = 32
    block = (n+TPB-1)//TPB
    crypto_gpu_compare[block,TPB](mean,median,crypto_value,out1,out2)

    #mean, median, dates, name
    crypto_gpu_graph_generator(out1, out2, gpu_dates_array, str(gpu_type))

    print('Function Completed:',gpu_type)

    return mean, median, gpu_type

#variable definitions need to be fixed since the functions they call have been updated

def main():

    crypto_data_gen()

    mean60, median60, gpu_type60, date = gpu_3060()
    mean70, median70, gpu_type70 = gpu_3070()
    mean80, median80, gpu_type80 = gpu_3080()
    mean90, median90, gpu_type90 = gpu_3090()

    n = mean60.size
    TPB = 32
    block = (n+TPB-1)//TPB
    
    #60-70
    out_mean = np.zeros(len(mean60))
    out_median = np.zeros(len(median60))
    gpu_diff[block,TPB](mean60, mean70, out_mean)
    gpu_diff[block,TPB](median60, median70, out_median)
    gpu_diff_graph(gpu_type60, gpu_type70, out_mean, out_median, date)

    #80-90
    out_mean2 = np.zeros(len(mean60))
    out_median2 = np.zeros(len(median60)) 
    gpu_diff[block,TPB](mean80, mean90, out_mean2)
    gpu_diff[block,TPB](median80, median90, out_median2)
    gpu_diff_graph(gpu_type80, gpu_type90, out_mean2, out_median2, date)


if __name__ == '__main__':
    main()

