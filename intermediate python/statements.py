# IF..................................................................................................................
# Examine the if statement that prints out "looking around in the kitchen." if room equals "kit".
# Write another if statement that prints out "big place!" if area is greater than 15.
# solution:
# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit" :
    print("looking around in the kitchen.")

# if statement for area
if area>15:
    print("big place!")

#     ELSE........................................
#     Add an else statement to the second control structure so that "pretty small." is printed out if area > 15 evaluates to False.
#solution:
# Define variables
room = "kit"
area = 14.0

# if-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
else :
    print("looking around elsewhere.")

# if-else construct for area
if area > 15 :
    print("big place!")
else :
    print("pretty small.")
   

# elif....................................................................................
# Add an elif to the second control structure such that "medium size, nice!" is printed out if area is greater than 10.
#solution:
# Define variables
room = "bed"
area = 14.0

# if-elif-else construct for room
if room == "kit" :
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else :
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15 :
    print("big place!")
elif area>10 :
    print("medium size, nice!")
else :
    print("pretty small.")


# driving right..........................................................................................................
# Extract the drives_right column as a Pandas Series and store it as dr.
# Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
# Print sel, and assert that drives_right is True for all observations.
# solution
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr= cars["drives_right"]

# Use dr to subset cars: sel
sel = cars [dr==True]

# Print sel
print(sel)

# Convert the code to a one-liner that calculates the variable sel as before
# solution:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]
# Print sel
print(sel)

# Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
# Use cpc in combination with a comparison operator and 500. You want to end up with a boolean Series that's True if the corresponding country has a cars_per_cap of more than 500 and False otherwise. Store this boolean Series as many_cars.
# Use many_cars to subset cars, similar to what you did before. Store the result as car_maniac.
# Print out car_maniac to see if you got it right.
#solution:
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]
# Print car_maniac
print(car_maniac)

# Cars per capita (2)
# 100xp
# Remember about np.logical_and(), np.logical_or() and np.logical_not(), the Numpy variants of the and, or and not operators? You can also use them on Pandas Series to do more advanced filtering operations.
# Take this example that selects the observations that have a cars_per_cap between 10 and 80. Try out these lines of code step by step to see what's happening.
# cpc = cars['cars_per_cap']
# between = np.logical_and(cpc > 10, cpc < 80)
# medium = cars[between]
# Instructions
# -Use the code sample above to create a DataFrame medium, that includes all the observations of cars that have a cars_per_cap between 100 and 500.
# -Print out medium.
# '''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]

# Print medium
print(medium)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Import numpy, you'll need this
import numpy as np

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 100, cpc < 500)
medium = cars[between]

# Print medium
print(medium)
