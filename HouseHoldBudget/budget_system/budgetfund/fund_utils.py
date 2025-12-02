# -----------------------------------------------------------
# Dev Log – fund_utils
#
# Wrote these helper functions mainly because the core budgetfund
# class was getting too crowded, and I didn’t want the display /
# filtering logic mixed in with the actual balance handling. 
# So this file is basically for “showing stuff nicely”.
#
# print_log():
#   Gets the dataframe from budgetfund.get_df().  
#   Added some simple color styling so succeeded rows are green
#   and failed ones red. The styling part is a bit hacky but works
#   fine in Jupyter. It returns the raw list data too because some
#   callers still need the values, not just the styled table.
#
# search_log():
#   Just a keyword search on the description column.  
#   Needed to fill in empty descriptions first, otherwise regex
#   matching complains. If nothing matches it returns a simple msg
#   instead of an empty styled df (looked weird).
#
# filter_status():
#   Very similar idea, just filters by succeeded/failed.
#   Reuses the same coloring so the output looks consistent.
#
# Overall: tried to keep things simple. No heavy logic here,
# mostly formatting + small filters. Should probably refactor
# later but good enough for now.
# -----------------------------------------------------------


from .budgetfund import budgetfund
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

def print_log(budgetfund,start,end):
    df = budgetfund.get_df(start,end)
    def color_status(val):
        if val == 'succeeded':
            return 'background-color: #d4edda; color: #155724;'
        elif val == 'failed':
            return 'background-color: #f8d7da; color: #721c24;'
        return ""
    styler = df.style
    styler = styler.map(color_status, subset="status")

    display(styler)

    return [df.values.tolist(), f"Total Record #: {len(df)}"]


def search_log(budgetfund, keyword=''):
    df = budgetfund.get_df().copy()
    df['description'] = df['description'].fillna("")
    found = df[df['description'].str.contains(keyword, case=False, na=False)]
    if found.empty:
        return ["No record found"]
    def color_status(val):
        if val == 'succeeded':
            return 'background-color: #d4edda; color: #155724;'
        elif val == 'failed':
            return 'background-color: #f8d7da; color: #721c24;'
        return ""
    styler = found.style.map(color_status, subset="status")
    display(styler)
    return [found.values.tolist(), f"Total # of Record Found is: {len(found)}"]
    

def filter_status(budgetfund, status=True):
    df = budgetfund.get_df().copy()
    target = 'succeeded' if status else 'failed'
    found = df[df['status'] == target]
    if found.empty:
        return "No record found"
    def color_status(val):
        if val == 'succeeded':
            return 'background-color: #d4edda; color: #155724;'
        elif val == 'failed':
            return 'background-color: #f8d7da; color: #721c24;'
        return ""
    styler = found.style.map(color_status, subset="status")
    display(styler)
    return [found.values.tolist(), f"Total # of Record Found is: {len(found)}"]
