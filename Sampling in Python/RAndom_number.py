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
