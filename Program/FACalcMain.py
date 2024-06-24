################################################################################
# AFROTC FITNESS ASSESSMENT CALCULATOR - MAIN
'''
Calculates FA scores from a csv file input. Completes assessment on push-ups,
sit-ups, and the 1.5 mile run. Additionally, it completes the appropriate
altitude adjustment. Can instantly calculate a list of scores for mass grading.

Aiden Seay - Summer 2024
'''
################################################################################
# IMPORTS
import Utilities.IOUtility as IO
import Utilities.ScoreUtility as Score

################################################################################
# CONSTANTS
from Utilities.Constants import *

################################################################################
# MAIN PROGRAM

def main():

    # display introduction
    print("FA CALCULATOR\n=============")

    # get the input data
    df = IO.import_data()

    # check if valid input
    if df.empty:
        return 0
    
    # initialize output csv file

    # iterate through each cadet row
    for index, row in df.iterrows():

        # get appropriate scoring table
        age = row[AGE]
        gender = row[GENDER]
        table = IO.import_table(age, gender)

        # start comparing
        


################################################################################
main()