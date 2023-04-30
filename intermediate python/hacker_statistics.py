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
