# Import pandas as pd.
# Use the pre-defined lists to create a dictionary called my_dict. There should be three key value pairs:
# key 'country' and value names.
# key 'drives_right' and value dr.
# key 'cars_per_cap' and value cpc.
# Use pd.DataFrame() to turn your dict into a DataFrame called cars.
# Print out cars and see how beautiful it is.
#solution:
# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Print cars
print(cars)

# Hit Run Code to see that, indeed, the row labels are not correctly set.
# Specify the row labels by setting cars.index equal to row_labels.
# Print out cars again and check if the row labels are correct this time.
#solution:
import pandas as pd

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print (cars)


# To import CSV files you still need the pandas package: import it as pd.
# Use pd.read_csv() to import cars.csv data as a DataFrame. Store this DataFrame as cars.
# Print out cars. Does everything look OK?
#solution:
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars= pd.read_csv('cars.csv')

# Print out cars
print(cars)



# Run the code with Run Code and assert that the first column should actually be used as row labels.
# Specify the index_col argument inside pd.read_csv(): set it to 0, so that the first column is used as row labels.
# Has the printout of cars improved now?
#solution:

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col=0)

# Print out cars
print(cars)
