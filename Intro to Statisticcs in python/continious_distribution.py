
# To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.


# Import uniform from scipy.stats and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called prob_less_than_5.

# Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.

# Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.\
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30
# Min and max wait times for back-up that happens every 30 min
min_time = 0
max_time = 30

# Import uniform from scipy.stats
from scipy.stats import uniform

# Calculate probability of waiting less than 5 mins
prob_less_than_5 =  uniform.cdf(5, min_time, max_time)
print(prob_less_than_5)