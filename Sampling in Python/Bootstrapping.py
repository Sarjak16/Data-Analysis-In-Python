# Generate a single bootstrap resample from spotify_sample.
# Generate 1 bootstrap resample
spotify_1_resample = spotify_sample.sample(n=len(spotify_sample), replace=True)


# Print the resample
print(spotify_1_resample)

