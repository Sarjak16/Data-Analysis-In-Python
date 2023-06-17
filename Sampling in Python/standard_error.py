
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

Calculate the standard deviation of popularity in 4 ways.

# Population: from spotify_population, take the standard deviation of popularity.
# Original sample: from spotify_sample, take the standard deviation of popularity.
# Sampling distribution: from sampling_distribution, take its standard deviation and multiply by the square root of the sample size (5000).
# Bootstrap distribution: from bootstrap_distribution, take its standard deviation and multiply by the square root of the sample size.
# Calculate the population std dev popularity
pop_sd = spotify_population['popularity'].std(ddof=0)

# Calculate the original sample std dev popularity
samp_sd = spotify_sample['popularity'].std()

# Calculate the sampling dist'n estimate of std dev popularity
samp_distn_sd = np.std(sampling_distribution, ddof=1) * np.sqrt(5000)

# Calculate the bootstrap dist'n estimate of std dev popularity
boot_distn_sd = np.std(bootstrap_distribution, ddof=1) * np.sqrt(5000)

# Print the standard deviations
print([pop_sd, samp_sd, samp_distn_sd, boot_distn_sd])
# Print the means
print([pop_mean, samp_mean, samp_distn_mean, boot_distn_mean])
