################################################################################
# AFROTC FITNESS ASSESSMENT CALCULATOR - Score Utility
'''
Performs all table lookups for the push-ups, sit-ups, and 1.5 mile run.
Aiden Seay - Summer 2024
'''
################################################################################
# IMPORTS
from datetime import datetime, timedelta

################################################################################
# CONSTANTS
from Utilities.Constants import *

################################################################################
# MAIN UTILITY FUNCTIONS

def lookup_push_up(table, count):

    # check if above the max
    if count > table.iloc[0][CHT_PU_REP]:
        score = table.iloc[0][CHT_PU_SCR]

    else:
        # has reached the min value
        try:
            row = table[table[CHT_PU_REP] == count]
            score = row[CHT_PU_SCR].values[0]

        # didn't achieve min value
        except:
            score = 0.0

    return score

def lookup_run(table, alt_table, time, alt):

    # complete altitude adjustment
    adj_time = adjust_altitude(time, alt_table, alt)

    rounded_time = round_time(adj_time, table, CHT_RUN_TIME)
    row = table[table[CHT_RUN_TIME] == rounded_time]
    score = row[CHT_RUN_SCR].values[0]

    return score, adj_time

def lookup_sit_up(table, count):
    
     # check if above the max
    if count > table.iloc[0][CHT_SU_REP]:
        score = table.iloc[0][CHT_SU_SCR]

    else:
        # has reached the min value
        try:
            row = table[table[CHT_SU_REP] == count]
            score = row[CHT_SU_SCR].values[0]

        # didn't achieve min value
        except:
            score = 0.0

    return score

################################################################################
# SUPPORTING UTILITY FUNCTIONS

def adjust_altitude(time, alt_table, alt):

    rounded_time = round_time(time, alt_table, ALT_TIME)

    row = alt_table[alt_table[ALT_TIME] == rounded_time]
    sub_time = row[f"adjust{alt}"].values[0]

    adj_time = subtract_time(time, sub_time)

    return adj_time


def compare_time(time1, time2):

    t1 = datetime.strptime(time1, "%M:%S")
    t2 = datetime.strptime(time2, "%M:%S")

    return  t1 >= t2 # return true if t1 is greater


def round_time(time, table, header):

    old_time = "00:00"

    for index, row in table.iterrows():

        table_time = row[header]

        # time < table_time and time > old_time
        if compare_time(table_time, time) and compare_time(time, old_time):
    
            return table_time
        
        old_time = table_time


def subtract_time(time1, time2):
    
    t1 = datetime.strptime(time1, "%M:%S")
    t2 = datetime.strptime(time2, "%M:%S")
    
    delta1 = timedelta(minutes=t1.minute, seconds=t1.second)
    delta2 = timedelta(minutes=t2.minute, seconds=t2.second)
    
    result_delta = delta1 - delta2
    result_minutes, result_seconds = divmod(result_delta.seconds, 60)
    return f"{result_minutes:02}:{result_seconds:02}"

################################################################################