#!/usr/bin/env python3

""" Docstring """



# imports one per line
from mining import *

#Test if the function "six_best_months" and "six_worth_months" return the correct list.
def test_goog():
    read_stock_data("GOOG", "data/GOOG.json")
    assert six_best_months() == [('2007/12', 693.76), ('2007/11', 676.55), ('2007/10', 637.38), ('2008/01', 599.42),
                                 ('2008/05', 576.29), ('2008/06', 555.34)]
    assert six_worst_months() == [('2004/08', 104.66),('2004/09', 116.38), ('2004/10', 164.52), ('2004/11', 177.09), ('2004/12', 181.01),
                                  ('2005/03', 181.18), ]



test_goog()
