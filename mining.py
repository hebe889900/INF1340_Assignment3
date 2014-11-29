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
    for x in file_records:
            volumn = x["Volumn"]
            close = x["Column"]
            date = x ["Date"]
            date = datetime.datetime.strptime(date, '%Y-%m-%d')

        ## How to put the price in one month into one tuple?
    return


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

