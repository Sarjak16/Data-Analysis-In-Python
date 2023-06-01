# Print the mean and standard deviation of the unemployment rates for each year.
# Print the mean and standard deviation of rates by year
print(unemployment.agg(["mean", "std"]))
# Print the mean and standard deviation of the unemployment rates for each year, grouped by continent.
# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby("continent").agg(["mean", "std"]))
