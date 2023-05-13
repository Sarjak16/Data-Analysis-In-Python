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
