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

























