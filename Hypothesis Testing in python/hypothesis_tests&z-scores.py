# Calculating the sample mean.........................................................................................
# Print the late_shipments dataset.
# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments in the sample; that is, the mean cases where the late column is "Yes".
# Print the late_shipments dataset
print(late_shipments)

# Calculate the proportion of late shipments
late_prop_samp =(late_shipments["late"] == "Yes").mean()

# Print the results
print(late_prop_samp)

# Calculating a z-score..............................................................................................
# Hypothesize that the proportion of late shipments is 6%.
# Calculate the standard error from the standard deviation of the bootstrap distribution.
# Calculate the z-score.
# Hypothesize that the proportion is 6%
late_prop_hyp = 0.06

# Calculate the standard error
std_error = np.std(late_shipments_boot_distn)

# Find z-score of late_prop_samp
z_score = (late_prop_samp - late_prop_hyp) / std_error

# Print z_score
print(z_score)
