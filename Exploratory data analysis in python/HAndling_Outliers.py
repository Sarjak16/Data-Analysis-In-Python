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


REMOVING OUTLIERS..................................................................................

# Find the 75th and 25th percentiles, saving as price_seventy_fifth and price_twenty_fifth respectively.

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate the IQR, storing it as prices_iqr.
# Find the 75th and 25th percentiles
price_upper_perc = planes["Price"].quantile(0.75)
price_lower_perc = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_upper_perc - price_lower_perc
# Calculate the upper and lower outlier thresholds.

# Find the 75th and 25th percentiles
price_seventy_fifth = planes["Price"].quantile(0.75)
price_twenty_fifth = planes["Price"].quantile(0.25)

# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)
# Remove the outliers from planes.
# Calculate iqr
prices_iqr = price_seventy_fifth - price_twenty_fifth

# Calculate the thresholds
upper = price_seventy_fifth + (1.5 * prices_iqr)
lower = price_twenty_fifth - (1.5 * prices_iqr)

# Subset the data
planes = planes[(planes["Price"] > lower) & (planes["Price"] < upper)]

print(planes["Price"].describe())
