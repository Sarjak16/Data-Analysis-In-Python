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

# random walk...............................................................................................
# Make a list random_walk that contains the first step, which is the integer 0.
# Finish the for loop:
# The loop should run 100 times.
# On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
# Next, let the if-elif-else construct update step for you.
# The code that appends step to random_walk is already coded.
# Print out random_walk.
#solution:
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# Use max() in a similar way to make sure that step doesn't go below zero if dice <= 2.
# Hit Submit Answer and check the contents of random_walk.
# solution:
# NumPy is imported, seed is set

# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0,step-1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)
    

