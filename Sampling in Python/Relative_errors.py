# ...............................................Calculating relative errors................................................................

# Generate a simple random sample from attrition_pop of fifty rows, setting the seed to 2022.
# Calculate the mean employee Attrition in the sample.
# Calculate the relative error between mean_attrition_srs50 and mean_attrition_pop as a percentage.
# Generate a simple random sample of 50 rows, with seed 2022
attrition_srs50 = attrition_pop.sample(n=50, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs50 = np.mean(attrition_srs50['Attrition'])

# Calculate the relative error percentage
rel_error_pct50 = abs(mean_attrition_srs50 - mean_attrition_pop) / mean_attrition_pop * 100

# Print rel_error_pct50
print(rel_error_pct50)


# Calculate the relative error percentage again. This time, use a simple random sample of one hundred rows of attrition_pop.
# Generate a simple random sample of 100 rows, with seed 2022
attrition_srs100 = attrition_srs100 = attrition_pop.sample(n=100, random_state=2022)

# Calculate the mean employee attrition in the sample
mean_attrition_srs100 =  np.mean(attrition_srs100['Attrition'])

# Calculate the relative error percentage
rel_error_pct100 =  abs((mean_attrition_srs100 - mean_attrition_pop) / mean_attrition_pop) * 100

# Print rel_error_pct100
print(rel_error_pct100)
