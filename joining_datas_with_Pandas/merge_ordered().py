# Use merge_ordered() to merge gdp and sp500 using a left join on year and date. Save the results as gdp_sp500.
# Print gdp_sp500 and look at the returns for the year 2018.
# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)

# Use merge_ordered(), again similar to before, to merge gdp and sp500 use the function's ability to interpolate missing data to forward fill the missing value for returns,
# assigning this table to the variable gdp_sp500.
# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left', fill_method='ffill')


# Print gdp_sp500
print (gdp_sp500)


# Subset the gdp_sp500 table, select the gdp and returns columns, and save as gdp_returns.
# Print the correlation matrix of the gdp_returns table using the .corr() method.


# Use merge_ordered() to merge gdp and sp500, interpolate missing value
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left',  fill_method='ffill')

# Subset the gdp and returns columns
gdp_returns = gdp_sp500[['gdp','returns']]

# Print gdp_returns correlation
print (gdp_returns.corr())
