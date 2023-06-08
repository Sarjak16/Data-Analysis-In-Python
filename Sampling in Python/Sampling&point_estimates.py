# SIMPLE SAMPLING WITH PANDAS.....................................................................................................................................
# Sample 1000 rows from spotify_population, assigning to spotify_sample.
# Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(n=1000)

# Print the sample
print(spotify_sample)

# Calculate the mean duration in minutes from spotify_population using pandas.
# Calculate the mean duration in minutes from spotify_sample using pandas.
# Sample 1000 rows from spotify_population
spotify_sample = spotify_population.sample(n=1000)

# Print the sample
print(spotify_sample)

# Calculate the mean duration in mins from spotify_population
mean_dur_pop = spotify_population['duration_minutes'].mean()

# Calculate the mean duration in mins from spotify_sample
mean_dur_samp = spotify_sample['duration_minutes'].mean()

# Print the means
print(mean_dur_pop)
print(mean_dur_samp)

# SAMPLING with NUMPY................................................................
# Create a pandas Series, loudness_pop, by subsetting the loudness column from spotify_population.
# Sample loudness_pop to get 100 random values, assigning to loudness_samp.
# Create a pandas Series from the loudness column of spotify_population
loudness_pop = pd.Series(spotify_population['loudness'])

# Sample 100 values of loudness_pop
loudness_samp = loudness_pop.sample(n=100)

# Print the sample
print(loudness_samp)

