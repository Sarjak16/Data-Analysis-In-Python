# Proportional stratified sampling......................................................................................................
# Get the proportion of employees by Education level from attrition_pop
# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts() / len(attrition_pop)

# Print education_counts_pop
print(education_counts_pop)

# Use proportional stratified sampling on attrition_pop to sample 40% of each Education group, setting the seed to 2022.
# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat =attrition_pop.groupby('Education').sample(frac=0.4, random_state=2022)


# Print the sample
print(attrition_strat)

# Get the proportion of employees by Education level from attrition_strat.
# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts(normalize=True)

# Print education_counts_pop
print(education_counts_pop)

# Proportional stratified sampling for 40% of each Education group
attrition_strat = attrition_pop.groupby('Education')\
	.sample(frac=0.4, random_state=2022)

# Calculate the Education level proportions from attrition_strat
education_counts_strat = attrition_strat['Education'].value_counts(normalize=True)

# Print education_counts_strat
print(education_counts_strat)


# Equal Counts Stratified And Sampling..............................................................................................................
# Use equal counts stratified sampling on attrition_pop to get 30 employees from each Education group, setting the seed to 2022.
# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby("Education").sample(n=30, random_state=2022)


# Print the sample
print(attrition_eq)

# Get the proportion of employees by Education level from attrition_eq.
# Get 30 employees from each Education group
attrition_eq = attrition_pop.groupby('Education')\
	.sample(n=30, random_state=2022)      

# Get the proportions from attrition_eq
education_counts_eq =  attrition_eq['Education'].value_counts() / len(attrition_eq)

# Print the results
print(education_counts_eq)


# WEIGHTED Sampling.............................................................................................................................................
# Plot YearsAtCompany from attrition_pop as a histogram with bins of width 1 from 0 to 40.
# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees from attrition_pop weighted by YearsAtCompany.
# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight =  attrition_pop.sample(n=400, weights='YearsAtCompany')

# Print the sample
print(attrition_weight)

# Plot YearsAtCompany from attrition_weight as a histogram with bins of width 1 from 0 to 40.

# Plot YearsAtCompany from attrition_pop as a histogram
attrition_pop['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()

# Sample 400 employees weighted by YearsAtCompany
attrition_weight = attrition_pop.sample(n=400, weights="YearsAtCompany")

# Plot YearsAtCompany from attrition_weight as a histogram
attrition_weight['YearsAtCompany'].hist(bins=np.arange(0, 41, 1))
plt.show()
