
# Dropping duplicates..............................................................
# Removing duplicates is an essential skill to get accurate counts because often, you don't want to count the same thing multiple times. 
#In this exercise, you'll create some new DataFrames using unique values from sales.

# sales is available and pandas is imported as pd.

# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
# Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates, saving as holiday_dates.
# Select the date column of holiday_dates, and print.

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=['store','type'])

print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset= ['store', 'department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates('date')

# Print date col of holiday_dates
print(holiday_dates['date'])





# Count the number of stores of each type
store_counts = store_types['type'].value_counts()
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)
