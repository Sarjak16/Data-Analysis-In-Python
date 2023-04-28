#while loop...............................................................................................
The while loop is like a repeated if statement. The code is executed over and over again, as long as the condition is True. Have another look at its recipe.

while condition :
    expression
Can you tell how many printouts the following while loop will do?

x = 1
while x < 4 :
    print(x)
    x = x + 1
    
    answer:
    3
    
#basic while loop
#Create the variable offset with an initial value of 8.
#Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
#Print out the sentence "correcting...".
#Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
#Finally, still within your loop, print out offset so you can see how it changes.

# Initialize offset
offset=8


# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)
    
# Inside the while loop, complete the if-else statement:
# If offset is greater than zero, you should decrease offset by 1.
# Else, you should increase offset by 1.
# If you've coded things correctly, hitting Submit Answer should work this time.
# If your code is still taking too long to run (or your session is expiring), you probably made a mistake. 
# Check your code and make sure that the statement offset != 0 will eventually evaluate to FALSE!
#solution:
# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset>0 :
      offset= offset - 1

    else : 
      offset= offset +1    
    print(offset)
    
#     For loop:.............................................................................................
#     Write a for loop that iterates over all elements of the areas list and prints out every element separately.
#     SOLUTION:
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
    print(area)

#     Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
# Update the print() statement so that on each run, a line of the form "room x: y" should be printed, where x is the index of the list element and y is the actual list element, i.e. the area. 
# Make sure to print out this exact string, with the correct spacing.
#solution:
# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index,a in enumerate(areas) :
    print("room " + str(index)+":"+str(a))
        

