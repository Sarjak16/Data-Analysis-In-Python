# Create a histogram with 10 bins to visualize the distribution of the amount. Show the plot.
# Histogram of amount with 10 bins and show plot
amir_deals['amount'].hist(bins=10)
plt.show()

#1
# What's the probability of Amir closing a deal worth less than $7500?
# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)

# 2
# What's the probability of Amir closing a deal worth more than $1000?
# Probability of deal > 1000
prob_over_1000 = 1- norm.cdf(1000, 5000, 2000)

print(prob_over_1000)

# 3
# What's the probability of Amir closing a deal worth between $3000 and $7000?
# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)

# 4
# What amount will 25% of Amir's sales be less than?
# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)
