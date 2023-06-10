# Generate 5000 numbers from a uniform distribution, setting the parameters low to -3 and high to 3.
# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Print uniforms
print(uniforms)

# Generate 5000 numbers from a normal distribution, setting the parameters loc to 5 and scale to 2.

# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Print normals
print(normals)

# Plot a histogram of uniforms with bins of width of 0.25 from -3 to 3 using plt.hist().
# Generate random numbers from a Uniform(-3, 3)
uniforms = np.random.uniform(low=-3, high=3, size=5000)

# Plot a histogram of uniform values, binwidth 0.25
plt.hist(uniforms, bins=np.arange(-3, 3.25, 0.25))
plt.show()

# Plot a histogram of normals with bins of width of 0.5 from -2 to 13 using plt.hist().
# Generate random numbers from a Normal(5, 2)
normals = np.random.normal(loc=5, scale=2, size=5000)

# Plot a histogram of normal values, binwidth 0.5
plt.hist(normals, bins= np.arange(-2, 13.5, 0.5))
plt.show()


# SIMPLE RANDOM SAMPLING...............................................................................
# Sample 70 rows from attrition_pop using simple random sampling, setting the random seed to 18900217.
# Print the sample dataset, attrition_samp. What do you notice about the indices?

# Sample 70 rows using simple random sampling and set the seed
attrition_samp = attrition_pop.sample(n=70, random_state=18900217)

# Print the sample
print(attrition_samp)

# SYSTEMATIC SAMPLING..........................................................................................................
# Set the sample size to 70.
# Calculate the population size from attrition_pop.
# Calculate the interval between the rows to be sampled.# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size // sample_size

# Systematically sample 70 rows
attrition_sys_samp = attrition_pop.iloc[::interval]

# Print the sample
print(attrition_sys_samp)

# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size//sample_size

# Systematically sample attrition_pop to get the rows of the population at each interval, starting at 0; assign the rows to attrition_sys_samp.
# Set the sample size to 70
sample_size = 70

# Calculate the population size from attrition_pop
pop_size = len(attrition_pop)

# Calculate the interval
interval = pop_size // sample_size

# Systematically sample 70 rows
attrition_sys_samp = attrition_pop.iloc[::interval]

# Print the sample
print(attrition_sys_samp)


# Add an index column to attrition_pop, assigning the result to attrition_pop_id.
# Create a scatter plot of YearsAtCompany versus index for attrition_pop_id using pandas .plot().
# Add an index column to attrition_pop
attrition_pop_id = attrition_pop.reset_index()

# Plot YearsAtCompany vs. index for attrition_pop_id
attrition_pop_id.plot(kind='scatter', x='index', y='YearsAtCompany')
plt.show()

# Randomly shuffle the rows of attrition_pop.
# Reset the row indexes, and add an index column to attrition_pop.
# Shuffle the rows of attrition_pop
attrition_shuffled = attrition_pop.sample(frac=1)

# Reset the row indexes and create an index column
attrition_shuffled = attrition_shuffled.reset_index(drop=True).reset_index()

# Plot YearsAtCompany vs. index for attrition_shuffled
attrition_shuffled.plot(kind="scatter", x="index", y="YearsAtCompany")
plt.show()
# Repeat the scatter plot of YearsAtCompany versus index, this time using attrition_shuffled.
