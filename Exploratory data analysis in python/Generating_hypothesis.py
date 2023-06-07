#Filter salaries where "Employee_Location" is "US" or "GB", saving as usa_and_gb.
#Use usa_and_gb to create a barplot visualizing "Salary_USD" against "Employee_Location"

# Filter for employees in the US or GB
usa_and_gb = salaries[salaries["Employee_Location"].isin(["US", "GB"])]

# Create a barplot of salaries by location
sns.barplot(data=usa_and_gb, x="Employee_Location", y="Salary_USD")
plt.show()

# Produce a barplot comparing "Salary_USD" by "Company_Size", factoring "Employment_Status".
# Create a bar plot of salary versus company size, factoring in employment status
sns.barplot(data=salaries, x="Company_Size", y="Salary_USD", hue="Employment_Status")
plt.show()

