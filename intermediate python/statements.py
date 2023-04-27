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
