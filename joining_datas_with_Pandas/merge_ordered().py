# Use merge_ordered() to merge gdp and sp500 using a left join on year and date. Save the results as gdp_sp500.
# Print gdp_sp500 and look at the returns for the year 2018.
# Use merge_ordered() to merge gdp and sp500 on year and date
gdp_sp500 = pd.merge_ordered(gdp, sp500, left_on='year', right_on='date', 
                             how='left')

# Print gdp_sp500
print(gdp_sp500)
