# Hypothesize that the proportion of late shipments is 6%.
# Calculate the sample proportion of shipments where late equals "Yes".
# Calculate the number of observations in the sample.
# Hypothesize that the proportion of late shipments is 6%
p_0 = 0.06

# Calculate the sample proportion of late shipments
p_hat = (late_shipments["late"] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Print p_hat and n
print(p_hat, n)


# Calculate the numerator and denominator of the z-score.
# Calculate the z-score as the ratio of these numbers.
# Calculate the sample proportion of late shipments
p_hat = (late_shipments['late'] == "Yes").mean()

# Calculate the sample size
n = len(late_shipments)

# Calculate the numerator and denominator of the test statistic
numerator = p_hat-p_0
denominator = np.sqrt(p_0 * (1- p_0)/n)

# Calculate the test statistic
z_score = numerator/denominator

# Print the result
print(z_score)
