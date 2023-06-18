# Generate a 95% confidence interval using the quantile method on the bootstrap distribution, 
# setting the 0.025 quantile as lower_quant and the 0.975 quantile as upper_quant.
# Generate a 95% confidence interval using the quantile method
lower_quant = np.quantile(bootstrap_distribution, 0.025)
upper_quant = np.quantile(bootstrap_distribution, 0.975)

# Print quantile method confidence interval
print((lower_quant, upper_quant))
