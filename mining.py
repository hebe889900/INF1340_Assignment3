#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime

stock_data = []
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
    file_records = read_json_from_file(stock_file_name)
    dic_for_records = {}
    for x in file_records:
        volume = x["Volume"]
        close = x["Close"]
        date = x["Date"]
        date = str(date)
        key = date[:7]
        dic_for_records = insertitem(key,volume,close,dic_for_records)
    for k,v in dic_for_records.items():
        average_price = v[0]/v[1] #Sales is divided by Volume
        monthly_averages.append((k,average_price))
        monthly_averages.sort(key=lambda tup: tup[1]) #Sort the list by average price
    return six_best_months(monthly_averages)




def insertitem(key,volume,close,dic):
    """
        The function will insert the items into dictionary.
        The key is the month in the data.
        The value is the tuple that contains two items: total sales of one month snd volume of sales per month.
    :param key: The month in the data
    :param volume: The volume of sales of one day for a stock
    :param close: The close price for a stock at the end of the day
    :param dic: The dictionary that stores all the parameters above in this function.
    :return:
    """
    list_1 = [volume*close,volume]
    dic.setdefault(key)
    dic[key] = [volume*close,volume]
    #if the date key is not the in the dictionary, add the key to it as well as the value of the key.
    return dic





def six_best_months(list):
    """
        This function is to identify the best siz months out of the monthly_averages list.
    :param list: The monthly_averages list
    :return: The last six items of the list
    """
    return list[-6:]


def six_worst_months(list):
    """
        This function is to identify the worst siz months out of the monthly_averages list.
    :param list: The monthly_averages list
    :return:
    """
    return list[0:6]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

print(read_stock_data("GOOG", "data/GOOG.json"))