# Detecting datatypes....................................................................
# Update the data type of the 2019 column of unemployment to float.
# Print the dtypes of the unemployment DataFrame again to check that the data type has been updated!
# Update the data type of the 2019 column to a float
unemployment["2019"] = unemployment["2019"].astype(float)
# Print the dtypes to check your work
print(unemployment.head())

# Define a Series of Booleans describing whether or not each continent is outside of Oceania; call this Series not_oceania.
# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])


# Use Boolean indexing to print the unemployment DataFrame without any of the data related to countries in Oceania.
# Define a Series describing whether each continent is outside of Oceania
not_oceania = ~unemployment["continent"].isin(["Oceania"])

# Print unemployment without records related to countries in Oceania
print(unemployment[not_oceania])
