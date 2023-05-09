#Pivoting on one variable...............................................................................................................................
# Pivot tables are the standard way of aggregating data in spreadsheets.

# In pandas, pivot tables are essentially another way of performing grouped calculations. That is, the .pivot_table() method is an alternative to .groupby().

# In this exercise, you'll perform calculations using .pivot_table() to replicate the calculations you performed in the last lesson using .groupby().

# sales is available and pandas is imported as pd.



# 1
# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type.
# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values= "weekly_sales", index= "type")

# Print mean_sales_by_type
print(mean_sales_by_type)


# 2
# Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values= "weekly_sales", index= "type", aggfunc= [np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# 3
# Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday.
# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales", index= "type", columns= "is_holiday")

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)


# Fill in missing values and sum values with pivot tables.........................................................................................................
# The .pivot_table() method has several useful arguments, including fill_value and margins.

# fill_value replaces missing values with a real value (known as imputation). What to replace missing values with is a topic big enough to have its own course (Dealing with Missing Data in Python), 
# but the simplest thing to do is to substitute a dummy value.
# margins is a shortcut for when you pivoted by two variables, but also wanted to pivot by each of those variables separately: 
#   it gives the row and column totals of the pivot table contents.
# In this exercise, you'll practice using these arguments to up your pivot table skills, which will help you crunch numbers more efficiently!

#sales is available and pandas is imported as pd.

#Print the mean weekly_sales by department and type, filling in any missing values with 0.
# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales", index= "department",  columns= "type", fill_value= 0))
