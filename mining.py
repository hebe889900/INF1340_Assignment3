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
    file_records = read_json_from_file(stock_file_name)
    dic_for_records = {}
    for x in file_records:
        volumn = x["Volumn"]
        close = x["Column"]
        date = x ["Date"]
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        key = getattr(date,"year")+"/"+getattr(date,"month")
        dic_for_records = insertitem(key,volumn,close,dic_for_records)
    for k,v in dic_for_records.items():
        average_price = v[0]/v[1] #Sales is divided by Volumn
        monthly_averages.append((k,average_price))
    return


def insertitem(key,volumn,close,dic):
    if key in dic:
        dic[key] = (dic[0]+cal_sales(volumn,close),dic[1]+volumn)
        #if the date key is already in the dictionary, add the sales to the total sales and the volumn to the total volumn.
    else:
        dic.setdefault(key,[]).append((cal_sales(volumn,close),volumn))
        #if the date key is not the in the dictionary, add the key to it as well as the value of the key.
    return dic

def cal_sales(volumn,close):
    sales = volumn * close
    return sales;




def six_best_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def six_worst_months():
    return [('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0), ('', 0.0)]


def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)

