# Print the mean and standard deviation of the unemployment rates for each year.
# Print the mean and standard deviation of rates by year
print(unemployment.agg(["mean", "std"]))
# Print the mean and standard deviation of the unemployment rates for each year, grouped by continent.
# Print yearly mean and standard deviation grouped by continent
print(unemployment.groupby("continent").agg(["mean", "std"]))

# Create a column called mean_rate_2021 which shows the mean 2021 unemployment rate for each continent.
# Create a column called std_rate_2021 which shows the standard deviation of the 2021 unemployment rate for each continent.

continent_summary = unemployment.groupby("continent").agg(
    # Create the mean_rate_2021 column
    mean_rate_2021 = ("2021", "mean"),
    # Create the std_rate_2021 column
     std_rate_2021= ("2021", "std"),
)
print(continent_summary)
