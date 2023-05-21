
# Import binom from scipy.stats and set the random seed to 10.
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 1 deal worked on by Amir, who wins 30% of the deals he works on.
# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate a single deal
print(binom.rvs(1, 0.3, size=1))


# Simulate a typical week of Amir's deals, or one week of 3 deals.

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 1 week of 3 deals
print(binom.rvs(3,0.3,size=1))

# Simulate a year's worth of Amir's deals, or 52 weeks of 3 deals each, and store in deals.
# Print the mean number of deals he won per week.

# Import binom from scipy.stats
from scipy.stats import binom

# Set random seed to 10
np.random.seed(10)

# Simulate 52 weeks of 3 deals
deals = binom.rvs(3,0.3,size=52)

# Print mean deals won per week
print(np.mean(deals))


# ..................................................................................................................................................................

# What's the probability that Amir closes all 3 deals in a week? Save this as prob_3.
# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3,3,0.3)

print(prob_3)
# What's the probability that Amir closes 1 or fewer deals in a week? Save this as prob_less_than_or_equal_1.

# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)

print(prob_less_than_or_equal_1)

# What's the probability that Amir closes more than 1 deal? Save this as prob_greater_than_1.


# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)

print(prob_greater_than_1)


# ..........................................................................................................................................................
# Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.
# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.
# Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%.

# Expected number won with 30% win rate
won_30pct = 3 * 0.3
print(won_30pct)

# Expected number won with 25% win rate
won_25pct = 3 * 0.25
print(won_25pct)

# Expected number won with 35% win rate
won_35pct = 3 * 0.35
print(won_35pct)
