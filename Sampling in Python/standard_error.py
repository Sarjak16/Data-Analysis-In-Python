
# Generate a sampling distribution of 2000 replicates.
# Sample 500 rows of the population without replacement and calculate the mean popularity.
mean_popularity_2000_samp = []

# Generate a sampling distribution of 2000 replicates
for i in range (2000):
    mean_popularity_2000_samp.append(
    	# Sample 500 rows and calculate the mean popularity 
    	spotify_population.sample(n=500, replace=False)['popularity'].mean()
    )

# Print the sampling distribution results
print(mean_popularity_2000_samp)
