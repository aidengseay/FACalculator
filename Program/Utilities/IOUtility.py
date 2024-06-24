################################################################################
# AFROTC FITNESS ASSESSMENT CALCULATOR - IO Utility
'''
Imports and exports FA data for program operations.
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

def import_data():

    csv_file_name = input("enter scorecard data .csv file: ")
    csv_file_path = f"../IO/{csv_file_name}"

    try:
        df = pd.read_csv(csv_file_path)
        return df

    except:
        print("\nerror, import file not found: program terminated")
        print("input data should be in IO directory")
        return pd.DataFrame()
    

def import_table(age, gender):

    rounded_age = round_age(age)
    try:
        df = pd.read_csv(f"../Tables/chart_{gender}_{rounded_age}.csv")
        return df

    except:
        print("\nerror, age out of range: program terminated")
        return pd.DataFrame()
    

def initialize_output():

    df = pd.DataFrame(columns=[NAME, GENDER, AGE, PU_REP, SU_REP, 
                               RUN_TIME, ALT, ADJ_RUN_TIME, PU_SCR, 
                               SU_SCR, RUN_SCR, TOT_SCR])
    
    return df



################################################################################
# SUPPORTING FUNCTIONS

def round_age(age):

    for index in range(len(AGES)):
        if age <= AGES[index]:
            return AGES[index]
        
    return None # age is too high to support

################################################################################