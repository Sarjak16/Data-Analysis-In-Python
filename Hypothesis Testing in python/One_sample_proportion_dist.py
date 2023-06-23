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
