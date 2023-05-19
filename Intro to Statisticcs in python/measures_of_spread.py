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
