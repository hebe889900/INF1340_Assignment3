#!/usr/bin/env python3

""" Docstring """



# imports one per line
import json
import datetime

stock_data = []
global monthly_averages
monthly_averages = []



def read_stock_data(stock_name, stock_file_name):
    """
        The function reads stock data from json files and it will create tuple with two items:
        average for each month and the date of the month.
        It will then append the tuple for each month to a list.
        It will also sort the list into display the best and worst 6 months.
    :param stock_name: string of the stock name
    :param stock_file_name: string of the json file which stores the stock information
    :return:
    """
    global monthly_averages
    monthly_averages = []
    file_records = read_json_from_file(stock_file_name)
    dic_for_records = {}
    for x in file_records:
        volume = x["Volume"]
        close = x["Close"]
        date = x["Date"]
        date = str(date)
        key = date[:7]
        key = key.replace("-","/")
        dic_for_records = insertitem(key,volume,close,dic_for_records)
    for k,v in dic_for_records.items():
        average_price = v[0]/v[1] #Sales is divided by Volume
        monthly_averages.append((k,float(format(average_price, '.2f'))))
        monthly_averages.sort(key=lambda tup: tup[1],reverse = True) #Sort the list by average price
    return




def insertitem(key,volume,close,dic):
    """
        The function will insert the items into dictionary.
        The key is the month in the data.
        The value is the tuple that contains two items: total sales of one month snd volume of sales per month.
    :param key: The month in the data
    :param volume: The volume of sales of one day for a stock
    :param close: The close price for a stock at the end of the day
    :param dic: The dictionary that stores all the parameters above in this function.
    :return: dictionary
    """
    if key in dic:
        dic[key] = [dic[key][0]+volume*close,dic[key][1]+volume]
    else:
        list_1 = [volume*close,volume]
        dic.setdefault(key)
        dic[key] = [volume*close,volume]
    #if the date key is not the in the dictionary, add the key to it as well as the value of the key.
    return dic



def six_best_months():
    """
        This function is to identify the best siz months out of the monthly_averages list.
        The best six is the six highest values in the monthly_averages list.
        The list is sorted from low values to high values.
    :param list: The monthly_averages list
    :return: The last six items on the list
    """
    monthly_averages.sort(key=lambda tup: tup[1],reverse = True)
    return monthly_averages[0:6]


def six_worst_months():
    """
        This function is to identify the worst siz months out of the monthly_averages list.
        The best six is the six highest values in the monthly_averages list.
        The list is sorted from low values to high values.
    :param list: The monthly_averages list
    :return: The first six items on the list
    """
    monthly_averages.sort(key=lambda tup: tup[1])
    return monthly_averages[0:6]


def read_json_from_file(file_name):
    """
        This function reads json file(file_name)and converts it to a python readable format.
    :param file_name: Name of the json file (file_name)
    :return: The json file in python readable format
    """
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

read_stock_data("GOOG", "data/GOOG.json")
