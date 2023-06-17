
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


# Generate a bootstrap distribution of 2000 replicates.
# Sample 500 rows of the sample with replacement and calculate the mean popularity.
mean_popularity_2000_boot = []

# Generate a bootstrap distribution of 2000 replicates
for i in range (2000):
    mean_popularity_2000_boot.append(
    	# Resample 500 rows and calculate the mean popularity     
    	spotify_sample.sample(n=500, replace=True)['popularity'].mean()
    )

# Print the bootstrap distribution results
print(mean_popularity_2000_boot)


# Calculate the mean popularity in 4 ways:

# Population: from spotify_population, take the mean of popularity.
# Sample: from spotify_sample, take the mean of popularity.
# Sampling distribution: from sampling_distribution, take its mean.
# Bootstrap distribution: from bootstrap_distribution, take its mean.
# Calculate the population mean popularity
pop_mean = np.mean(spotify_population['popularity'])

# Calculate the original sample mean popularity
samp_mean = np.mean(spotify_sample['popularity'])

# Calculate the sampling dist'n estimate of mean popularity
samp_distn_mean = np.mean(sampling_distribution)

# Calculate the bootstrap dist'n estimate of mean popularity
boot_distn_mean = np.mean(bootstrap_distribution)

# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])
