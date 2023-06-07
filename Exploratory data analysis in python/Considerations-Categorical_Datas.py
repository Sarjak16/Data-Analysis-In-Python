# Print the relative frequency of the "Job_Category" column from salaries DataFrame.
# Print the relative frequency of Job_Category
print(salaries["Job_Category"].value_counts(normalize=True))


#Cross Tabulation.............................................................................................................
# Perform cross-tabulation, setting "Company_Size" as the index, and the columns to classes in "Experience".
# Cross-tabulate Company_Size and Experience
print(pd.crosstab(salaries["Company_Size"], salaries["Experience"]))

# Cross-tabulate "Job_Category" and classes of "Company_Size" as column names.
# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"]))
# Update pd.crosstab() to return the mean "Salary_USD" values.
# Cross-tabulate Job_Category and Company_Size
print(pd.crosstab(salaries["Job_Category"], salaries["Company_Size"],
            values=salaries["Salary_USD"], aggfunc="mean"))
