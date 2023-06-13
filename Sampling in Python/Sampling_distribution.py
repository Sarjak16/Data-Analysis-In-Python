# Replicating samples...........................................................................
# Replicate the provided code so that it runs 500 times. Assign the resulting list of sample means to mean_attritions.
# Create an empty list
mean_attritions=[]
# Loop 500 times to create 500 sample means
for i in range(500):
	mean_attritions.append(
    	attrition_pop.sample(n=60)['Attrition'].mean()
	)
  
# Print out the first few entries of the list
print(mean_attritions[0:5])
