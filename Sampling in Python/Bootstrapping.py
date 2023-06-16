# Generate a single bootstrap resample from spotify_sample.
# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(n=len(spotify_sample), replace=True)


# Print the resample
print(spotify_1_resample)

# Calculate the mean of the danceability column of spotify_1_resample using numpy.
# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(frac=1, replace=True)

# Calculate of the danceability column of spotify_1_resample
mean_danceability_1 = np.mean(spotify_1_resample['danceability'])

# Print the result
print(mean_danceability_1)

# Replicate the expression provided 1000 times.
