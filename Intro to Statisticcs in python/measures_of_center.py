# Mean and median....................................................................................................................
# Import numpy with the alias np.
# Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that holds rows for 'USA'. Call these be_consumption and usa_consumption.
# Calculate the mean and median of kilograms of food consumed per person per year for both countries.

# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country'] == 'Belgium'] 

# Filter for USA
usa_consumption = food_consumption[food_consumption['country'] == 'USA'] 

# Calculate mean and median consumption in Belgium
print(np.mean(be_consumption['consumption']))
print(np.median(be_consumption['consumption']))

# Calculate mean and median consumption in USA
print(np.mean(usa_consumption['consumption']))
print(np.median(usa_consumption['consumption']))

# Subset food_consumption for rows with data about Belgium and the USA.
# Group the subsetted data by country and select only the consumption column.
# Calculate the mean and median of the kilograms of food consumed per person per year in each country using .agg().

# Import numpy as np
import numpy as np

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country']== 'Belgium') | (food_consumption['country']== 'USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))



# Import matplotlib.pyplot with the alias plt.
# Subset food_consumption to get the rows where food_category is 'rice'.
# Create a histogram of co2_emission for rice and show the plot.

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category']== 'rice']

# Histogram of co2_emission for rice and show plot
rice_consumption.co2_emission.hist()
plt.show()


# Use .agg() to calculate the mean and median of co2_emission for rice.
# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']

# Calculate mean and median of co2_emission with .agg()
print(rice_consumption.agg([np.mean, np.median]))
