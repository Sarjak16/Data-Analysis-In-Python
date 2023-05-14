# Total riders in a month.......................................................................
# Your goal is to find the total number of rides provided to passengers passing through the Wilson station (station_name == 'Wilson')
# when riding Chicago's public transportation system on weekdays (day_type == 'Weekday') in July (month == 7). Luckily, Chicago provides this detailed data, 
# but it is in three different tables. You will work on merging these tables together to answer the question. This data is different from the business related 
# data you have seen so far, but all the information you need to answer the question is provided.

# The cal, ridership, and stations DataFrames have been loaded for you. The relationship between the tables can be seen in the diagram below.



# Merge the ridership and cal tables together, starting with the ridership table on the left and save the result to the variable ridership_cal.
# If you code takes too long to run, your merge conditions might be incorrect.

# Merge the ridership and cal tables
ridership_cal = ridership.merge(cal )
