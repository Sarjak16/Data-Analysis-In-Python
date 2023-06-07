# ..........................................EXTRACTING FEATURES FOR CORRELATION......................................................................

# Extract the month from "date_of_response", storing it as a column called "month".
# Create the "weekday" column, containing the weekday that the participants completed the survey.
# Plot a heat map, including the Pearson correlation coefficient scores.
# Get the month of the response
salaries["month"] = salaries["date_of_response"].dt.month

# Extract the weekday of the response
salaries["weekday"] = salaries["date_of_response"].dt.weekday

# Create a heatmap
sns.heatmap(salaries.corr(), annot=True)
plt.show()

# Calculating Percentiles............................................
# Find the 25th percentile of "Salary_USD".
# Store the median of "Salary_USD" as salaries_median.
# Get the 75th percentile of salaries.
# Find the 25th percentile
twenty_fifth = salaries["Salary_USD"].quantile(.25)

# Save the median
salaries_median = salaries["Salary_USD"].median()

# Gather the 75th percentile
seventy_fifth = salaries["Salary_USD"].quantile(.75)
print(twenty_fifth, salaries_median, seventy_fifth)
