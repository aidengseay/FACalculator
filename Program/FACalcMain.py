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
import Utilities.IOUtility as io
import Utilities.ScoreUtility as score

################################################################################
# CONSTANTS
from Utilities.Constants import *

################################################################################
# MAIN PROGRAM

def main():

    print("FA CALCULATOR\n=============")
    df = io.import_data()

    if df.empty:
        return 0
    
    out_df = io.initialize_output()
    alt_table = io.import_alt_table()

    # iterate through each cadet row
    for index, row in df.iterrows():

        # get appropriate scoring table
        age = row[AGE]
        gender = row[GENDER]
        table = io.import_table(age, gender)

        if table.empty:
            return 0
        
        # calculate scores
        push_up_score = score.lookup_push_up(table, row[PU_REP])
        sit_up_score = score.lookup_sit_up(table, row[SU_REP])
        run_score, adj_time = score.lookup_run(table, alt_table, row[RUN_TIME], 
                                                                       row[ALT])

        total_score = push_up_score + sit_up_score + run_score

        # add to the output data frame
        new_row = {NAME:row[NAME], GENDER:row[GENDER], 
                   AGE:row[AGE], PU_REP:row[PU_REP], 
                   SU_REP:row[SU_REP], RUN_TIME:row[RUN_TIME],
                   ALT:row[ALT], ADJ_RUN_TIME:adj_time, 
                   PU_SCR:push_up_score, SU_SCR:sit_up_score, 
                   RUN_SCR:run_score, TOT_SCR:total_score}
        
        out_df.loc[len(out_df)] = new_row

    # export data into a csv
    print("program success -> results in IO/FA_Results.csv")
    output_file = "../IO/FA_Results.csv"
    out_df.to_csv(output_file, index=False)       


################################################################################
main()