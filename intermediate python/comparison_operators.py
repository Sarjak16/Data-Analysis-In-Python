# EQUALITY......................................................................................................................
# In the editor on the right, write code to see if True equals False.
# Write Python code to check if -5 * 15 is not equal to 75.
# Ask Python whether the strings "pyscript" and "PyScript" are equal.
# What happens if you compare booleans and integers? Write code to see if True and 1 are equal.
# Solution:
# Comparison of booleans

True==False

# Comparison of integers
-5*15!=75

# Comparison of strings
"pyscript"=="PyScript"

# Compare a boolean with an integer
True==1

# grater and less.....................................................................................................
# Write Python expressions, wrapped in a print() function, to check whether:
# x is greater than or equal to -10. x has already been defined for you.
# "test" is less than or equal to y. y has already been defined for you.
# True is greater than False.
#solution:
# Comparison of integers
x = -3 * 6
print(x>=-10)

# Comparison of strings
y = "test"
print("test"<=y)

# Comparison of booleans
print(True>False)

# Using comparison operators, generate boolean arrays that answer the following questions:

# Which areas in my_house are greater than or equal to 18?
# You can also compare two NumPy arrays element-wise. Which areas in my_house are smaller than the ones in your_house?
# Make sure to wrap both commands in a print() statement so that you can inspect the output!
#solution:
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house>=18)

# my_house less than your_house
print(my_house< your_house)

# Boolean...................................................................
# Write Python expressions, wrapped in a print() function, to check whether:
# my_kitchen is bigger than 10 and smaller than 18.
# my_kitchen is smaller than 14 or bigger than 17.
# double the area of my_kitchen is smaller than triple the area of your_kitchen.
#solution:
# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen>10 and my_kitchen<18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen<14 or my_kitchen>17)

# Double my_kitchen smaller than triple your_kitchen?
print(2*my_kitchen or 3*your_kitchen)

# Generate boolean arrays that answer the following questions:
# Which areas in my_house are greater than 18.5 or smaller than 10?
# Which areas are smaller than 11 in both my_house and your_house? Make sure to wrap both commands in print() statement, so that you can inspect the output.
# #solution
# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5,
                    my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11,
                     your_house < 11))
