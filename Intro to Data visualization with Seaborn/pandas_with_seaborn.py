# tidy vs untidy data............................................................................
# Read the csv file located at csv_filepath into a DataFrame named df.
# Print the head of df to show the first five rows.

# Import pandas
import pandas as pd

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Print the head of df
print(df.head())


# making countplot with dataframes......................................................................................
# # Import Matplotlib, pandas, and Seaborn using the standard names.
# # Create a DataFrame named df from the csv file located at csv_filepath.
# # Use the countplot() function with the x= and data= arguments to create a count plot with the "Spiders" column values on the x-axis.
# # Display the plot.

# Import Matplotlib, pandas, and Seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a DataFrame from csv file
df = pd.read_csv(csv_filepath)

# Create a count plot with "Spiders" on the x-axis
sns.countplot(x="Spiders", data=df)

# Display the plot
plt.show()
