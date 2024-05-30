# FA Calculator

**Disclaimer: Not affiliated with the US Government or the Air Force**

Calculates Air Force Fitness Assessment scores for ROTC. The fitness assessment
consists of push-ups, sit-ups, and a 1.5 mile run. This program will read in a
.csv file. 

## Formatting

### 

### How to Format the Input File

The format for the .csv file used for program input is below:

`cadet name, gender, age, # of push-ups, # of sit-ups, run time, alt group`

So an example would be:

`"Smith, Joe", M, 20, 56, 60, 9:30, 4`

### Format of Output File

The format for the .csv file used for program output is below:

`cadet name, gender, age, # of push-ups, # of sit-ups, run time, alt group, push-up score, sit-up score, run score, total score`

So an example would be:

`"Smith, Joe", M, 20, 56, 60, 9:30, 4, 17.8, 20, 60, 97.8`

## Limitations

The limitations (for now) are below: 
* Only calculates males and females up to 29 years old.
* Only calculates group 4 altitude adjustment
