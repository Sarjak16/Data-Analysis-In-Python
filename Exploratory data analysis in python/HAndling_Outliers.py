# IDENTIFYING OUTLIERS........................................................................
# Plot the distribution of "Price" column from planes.
# Plot a histogram of flight prices
sns.histplot(x="Price", data=planes)
plt.show()

# Display the descriptive statistics for flight duration.
# Plot a histogram of flight prices
sns.histplot(data=planes, x="Price")
plt.show()

# Display descriptive statistics for flight duration
print(planes['Duration'].describe())
