################################################################################
# AFROTC FITNESS ASSESSMENT CALCULATOR - Score Utility
'''
Performs all table lookups for the push-ups, sit-ups, and 1.5 mile run.
Aiden Seay - Summer 2024
'''
################################################################################
# IMPORTS
import pandas as pd

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

def lookup_run(table, time):

    return None, None

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


################################################################################