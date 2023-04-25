#Motivation for dictionaries:...................................................................................................................
#  Use the index() method on countries to find the index of 'germany'. Store this index as ind_ger.
# Use ind_ger to access the capital of Germany from the capitals list. Print it out.
#solution:

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Get index of 'germany': ind_ger
ind_ger=countries.index("germany")

# Use ind_ger to print out capital of Germany
print(capitals[ind_ger])

# With the strings in countries and capitals, create a dictionary called europe with 4 key:value pairs. 
#   Beware of capitalization! Make sure you use lowercase characters everywhere.
# Print out europe to see if the result is what you expected.
#solution:

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin','norway':'oslo' }

# Print europe
print(europe)

# Check out which keys are in europe by calling the keys() method on europe. Print out the result.
# Print out the value that belongs to the key 'norway'.

#solution
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Print out the keys in europe
print(europe.keys())

# Print out value that belongs to key 'norway'
print(europe['norway'])



