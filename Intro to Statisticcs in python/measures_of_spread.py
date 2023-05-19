# Quartiles, quantiles, and quintiles

# Calculate the quartiles of the co2_emission column of food_consumption

# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],np.linspace(0, 1, 5)))

# Calculate the six quantiles that split up the data into 5 pieces (quintiles) of the co2_emission column of food_consumption.
# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'],np.linspace(0, 1, 6)))


# Calculate the eleven quantiles of co2_emission that split up the data into ten pieces (deciles).
# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'],np.linspace(0, 1, 11)))


# varience na std
# Calculate the variance and standard deviation of co2_emission for each food_category by grouping and aggregating.
# Import matplotlib.pyplot with alias plt.
# Create a histogram of co2_emission for the beef food_category and show the plot.
# Create a histogram of co2_emission for the eggs food_category and show the plot.

# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
food_consumption[food_consumption['food_category'] == 'beef']['co2_emission'].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category'] == 'eggs']['co2_emission'].hist();
# Show plot
plt.show()
