#Random float.........................................................................................................................

# Import numpy as np.
# Use seed() to set the seed; as an argument, pass 123.
# Generate your first random float with rand() and print it out.
# solution:

# Import numpy as np
import numpy as np

# Set the seed
coin=np.random.seed(123)


# Generate and print random float
print(np.random.rand())


# Roll the dice.....................................................................................................................
# Use randint() with the appropriate arguments to randomly generate the integer 1, 2, 3, 4, 5 or 6. This simulates a dice. Print it out.
# Repeat the outcome to see if the second throw is different. Again, print out the result.
# solution:
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Roll the dice. Use randint() to create the variable dice.
# Finish the if-elif-else construct by replacing ___:
# If dice is 1 or 2, you go one step down.
# if dice is 3, 4 or 5, you go one step up.
# Else, you throw the dice again. The number of eyes is the number of steps you go up.
# Print out dice and step. Given the value of dice, was step updated correctly?
#solution:
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice<5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

