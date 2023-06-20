# Calculate a 95% confidence interval from late_shipments_boot_distn using the quantile method, labeling the lower and upper intervals lower and upper.

# Calculate 95% confidence interval using quantile method
lower = np.quantile(late_shipments_boot_distn, 0.025)
upper = np.quantile(late_shipments_boot_distn, 0.975)

# Print the confidence interval
print((lower, upper))


# T-test............................................................................................
# The sample means for the two groups are available as xbar_no and xbar_yes. The sample standard deviations are s_no and s_yes.
# The sample sizes are n_no and n_yes. numpy is also loaded as np.

# Calculate the numerator of the 
#  test statistic.
# Calculate the denominator of the 
#  test statistic.
# Use those two numbers to calculate the 
#  test statistic.

# Calculate the numerator of the test statistic
numerator = xbar_yes - xbar_no

# Calculate the denominator of the test statistic
denominator = np.sqrt(((s_no**2) / n_no) + ((s_yes**2) / n_yes))

# Calculate the test statistic
t_stat = numerator/denominator

# Print the test statistic
print(t_stat)
