# Import divorce.csv, saving as a DataFrame,
# divorce; indicate in the import function that the divorce_date, dob_man, dob_woman, and marriage_date columns should be imported as DateTime values.
# Import divorce.csv, parsing the appropriate columns as dates in the import
divorce = pd.read_csv("divorce.csv", parse_dates=['divorce_date', 'dob_man', 'dob_woman', 'marriage_date'] )

print(divorce.dtypes)

# Convert the marriage_date column of the divorce DataFrame to DateTime values.
# Convert the marriage_date column to DateTime values
divorce["marriage_date"] = pd.to_datetime(divorce["marriage_date"])

# Define a column called marriage_year, which contains just the year portion of the marriage_date column.
# Define the marriage_year column
divorce["marriage_year"] = divorce['marriage_date'].dt.year

# Define the marriage_year column
divorce["marriage_year"] = divorce["marriage_date"].dt.year

# Create a line plot showing the average number of kids by year
sns.lineplot(data=divorce, y="num_kids", x="marriage_year")
plt.show()
