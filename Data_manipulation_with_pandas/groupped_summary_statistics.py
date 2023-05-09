# What percent of sales occurred at each store type?
# While .groupby() is useful, you can calculate grouped summary statistics without it.

# Walmart distinguishes three types of stores: "supercenters," "discount stores," and "neighborhood markets," 
#   encoded in this dataset as type "A," "B," and "C." In this exercise, you'll calculate the total sales made at each store type, without using .groupby().
#   You can then use these numbers to see what proportion of Walmart's total sales were made at each type.

# sales is available and pandas is imported as pd.

# Instructions

# Calculate the total weekly_sales over the whole dataset.
# Subset for type "A" stores, and calculate their total weekly sales.
# Do the same for type "B" and type "C" stores.
# Combine the A/B/C results into a list, and divide by sales_all to get the proportion of sales by type.

# Calc total weekly sales
sales_all = sales["weekly_sales"].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"]== "B"]["weekly_sales"].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"]== "c"]["weekly_sales"].sum()

    # Get proportion for each type
    sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
    print(sales_propn_by_type)

    
#     Calculations with .groupby()........................................................................................................................
# The .groupby() method makes life much easier. In this exercise, you'll perform the same calculations as last time, except you'll use the .groupby() method.
# You'll also perform calculations on data grouped by two variables to see if sales differ by store type depending on if it's a holiday week or not.

# sales is available and pandas is loaded as pd.
# Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
# Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type.

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type/ sum(sales.weekly_sales)
print(sales_propn_by_type)

#Group sales by "type" and "is_holiday", take the sum of weekly_sales, and store as sales_by_type_is_holiday.

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type", "is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)


# Multiple grouped summaries...................................................................................................
# Earlier in this chapter, you saw that the .agg() method is useful to compute multiple statistics on multiple variables. 
# It also works with grouped data. NumPy, which is imported as np, has many different summary statistics functions, including: np.min, np.max, np.mean, and np.median.

# sales is available and pandas is imported as pd.

# Import numpy with the alias np.
# Get the min, max, mean, and median of weekly_sales for each store type using .groupby() and .agg(). Store this as sales_stats. Make sure to use numpy functions!
# Get the min, max, mean, and median of unemployment and fuel_price_usd_per_l for each store type. Store this as unemp_fuel_stats.

# Import numpy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)


