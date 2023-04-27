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



