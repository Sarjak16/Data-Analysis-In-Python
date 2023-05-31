# .............................................................................Functions for initial exploration........................................................

# Use a pandas function to print the first five rows of the unemployment DataFrame.
# Print the first five rows of unemployment
print(unemployment.head())

# Use a pandas function to print a summary of column non-missing values and data types from the unemployment DataFrame.
# Print a summary of non-missing values and data types in the unemployment DataFrame
print(unemployment.info())

# Print the summary statistics (count, mean, standard deviation, min, max, and quartile values) of each numerical column in unemployment.
# Print summary statistics for numerical columns in unemployment
print(unemployment.describe())



#Counting categorical values...............................................................
# Use a pandas function to count the values associated with each continent in the unemployment DataFrame.
# Count the values associated with each continent in unemployment
print(unemployment.continent.value_counts())


# Import the required visualization libraries.
# Create a histogram of the distribution of 2021 unemployment percentages across all countries in unemployment; show a full percentage point in each bin.
# Import the required visualization libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Create a histogram of 2021 unemployment; show a full percent in each bin
sns.histplot(data=unemployment, x="2021", binwidth=1)
plt.show()
