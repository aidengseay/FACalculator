# FA Calculator

**Disclaimer: Not affiliated with the US Government or the Air Force**

Calculates Air Force Fitness Assessment scores for ROTC. The fitness assessment
consists of push-ups, sit-ups, and a 1.5 mile run. This program will read in a
.csv file. 

## Formatting

### How to Format the Input File

The format for the .csv file used for program input is below:

`Cadet Name (Last, First), Gender, Age, Push-Up Rep, Sit-Up Rep, Run Time, Altitude`

So an example would be:

`"Smith, Joe", M, 20, 56, 60, 9:30, 4`

![Screenshot 2024-06-23 122640](https://github.com/aidengseay/FACalculator/assets/108606344/433602e5-1c6b-4ce0-8ab0-3f02738243cd)

### Format of Output File

The format for the .csv file used for program output is below:

`Cadet Name (Last, First), Gender, Age, Push-Up Rep, Sit-Up Rep, Run Time, Altitude, Run Time Adjusted, Push-Up Score, Sit-Up Score, Run Score, Total Score`

So an example would be:

`"Smith, Joe", M, 20, 56, 60, 9:30, 4, 17.8, 20, 60, 97.8`

### Template

The link [here](https://docs.google.com/spreadsheets/d/1c8SRzbzgjGFrWn_AW2ahf8LjR0iC29SsXAPMgh3-7_k/edit?usp=sharing) is a google sheet template!
* Make a copy of the template and fill it out 
* After filling out the google sheet download it as a .csv file

## Limitations

The limitations (for now) are below: 
* Only calculates males and females up to 29 years old.
* Only accounts for push-ups, sit-ups, and the 1.5 mile run.
