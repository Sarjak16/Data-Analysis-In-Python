#Labels................................................................................................................................................
# The strings xlab and ylab are already set for you. Use these variables to set the label of the x- and y-axis.
# The string title is also coded for you. Use it to add a title to the plot.
# After these customizations, finish the script with plt.show() to actually display the plot.

#SOLUTION:
# Basic scatter plot, log scale
plt.scatter(gdp_cap, life_exp)
plt.xscale('log') 

# Strings
xlab = 'GDP per Capita [in USD]'
ylab = 'Life Expectancy [in years]'
title = 'World Development in 2007'

# Add axis labels
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')

# Add title
plt.title('World Development in 2007')

# After customizing, display the plot
plt.show()

# TICKS......................................................................................................
# Use tick_val and tick_lab as inputs to the xticks() function to make the the plot more readable.
# As usual, display the plot with plt.show() after you've added the customizations.
#solution:
# Scatter plot
plt.scatter(gdp_cap, life_exp)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')

# Definition of tick_val and tick_lab
tick_val = [1000, 10000, 100000]
tick_lab = ['1k', '10k', '100k']

# Adapt the ticks on the x-axis
plt.xticks(tick_val,tick_lab)


# After customizing, display the plot
plt.show()

#sizes........................................................................................................................
# Run the script to see how the plot changes.
# Looks good, but increasing the size of the bubbles will make things stand out more.
# Import the numpy package as np.
# Use np.array() to create a numpy array from the list pop. Call this NumPy array np_pop.
# Double the values in np_pop setting the value of np_pop equal to np_pop * 2. Because np_pop is a NumPy array, each array element will be doubled.
# Change the s argument inside plt.scatter() to be np_pop instead of pop.

#SOLUTION:
# Import numpy as np
import numpy as np

# Store pop as a numpy array: np_pop
np_pop=np.array(pop)

# Double np_pop
np_pop=np_pop*2

# Update: set s argument to np_pop
plt.scatter(gdp_cap, life_exp, s = np_pop)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])

# Display the plot
plt.show()


#colors...........................................................................................................................
# Add c = col to the arguments of the plt.scatter() function.
# Change the opacity of the bubbles by setting the alpha argument to 0.8 inside plt.scatter(). 
# Alpha can be set from zero to one, where zero is totally transparent, and one is not at all transparent.

# Specify c and alpha inside plt.scatter()
plt.scatter(x = gdp_cap, y = life_exp, s = np.array(pop) * 2,c=col,alpha=0.8)

# Previous customizations
plt.xscale('log') 
plt.xlabel('GDP per Capita [in USD]')
plt.ylabel('Life Expectancy [in years]')
plt.title('World Development in 2007')
plt.xticks([1000,10000,100000], ['1k','10k','100k'])

# Show the plot
plt.show()

















