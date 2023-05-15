# first inner join ........................................................................................
# Merge taxi_owners with taxi_veh on the column vid, and save the result to taxi_own_veh.

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(taxi_veh, on= 'vid')

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)


# Set the left and right table suffixes for overlapping columns of the merge to _own and _veh, respectively.

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes= ('_own', '_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)


# Select the fuel_type column from taxi_own_veh and print the value_counts() to find the most popular fuel_types used.

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())


# Merge wards and census on the ward column and save the result to wards_census.

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on='ward')

# Print the shape of wards_census
print('wards_census table shape:', wards_census.shape)


# Merge the wards_altered and census tables on the ward column, and notice the difference in returned rows.

# Print the first few rows of the wards_altered table to view the change 
print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
wards_altered_census = wards_altered.merge(census, on='ward')

# Print the shape of wards_altered_census
print('wards_altered_census table shape:', wards_altered_census.shape)


#Merge the wards and census_altered tables on the ward column, and notice the difference in returned rows.
# Print the first few rows of the census_altered table to view the change 
print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
wards_census_altered = wards.merge( census_altered, on='ward')

# Print the shape of wards_census_altered
print('wards_census_altered table shape:', wards_census_altered.shape)





# left join..................................................................................................................................
# Merge the movies table, as the left table, with the financials table using a left join, and save the result to movies_financials.

# Merge movies and financials with a left join
movies_financials = movies.merge(financials, on='id', how='left')

#Count the number of rows in movies_financials with a null value in the budget column.

# Merge the movies table with the financials table with a left join
movies_financials = movies.merge(financials, on='id', how='left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isnull().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# enriching dataset.........................................................................................................................
#Merge toy_story and taglines on the id column with a left join, and save the result as toystory_tag.

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(taglines, on='id', how='left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)
