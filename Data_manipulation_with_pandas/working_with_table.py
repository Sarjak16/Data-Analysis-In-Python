# Add a year column to temperatures, from the year component of the date column.
# Make a pivot table of the avg_temp_c column, with country and city as rows, and year as columns. Assign to temp_by_country_city_vs_year, and look at the result.

# Add a year column to temperatures
temperatures['year']= temperatures['date'].dt.year

# Pivot avg_temp_c by country and city vs year
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c', index=['country','city'], columns='year')

# See the result
print(temp_by_country_city_vs_year)


# Use .loc[] on temp_by_country_city_vs_year to take subsets.

# From Egypt to India.
# From Egypt, Cairo to India, Delhi.
# From Egypt, Cairo to India, Delhi, and 2005 to 2010.
# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]

# Subset for Egypt, Cairo to India, Delhi, and 2005 to 2010
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']
