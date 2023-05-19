# calculating probablities.................................................................................................................
# Count the number of deals Amir worked on for each product type and store in counts.
# Count the deals for each product
counts = amir_deals['product'].value_counts()
print(counts)

# Calculate the probability of selecting a deal for the different product types by dividing the counts by the total number of deals Amir worked on. Save this as probs.
# Count the deals for each product
counts = amir_deals['product'].value_counts()

# Calculate probability of picking a deal with each product
probs = counts / len(amir_deals['product'])
print(probs)

# sampling deals.........................................................................................................\
# Set the random seed to 24.
# Take a sample of 5 deals without replacement and store them as sample_without_replacement.
# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5, replace=False)
print(sample_without_replacement)
