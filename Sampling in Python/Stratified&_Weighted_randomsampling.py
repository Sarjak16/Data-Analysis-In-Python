# Proportional stratified sampling......................................................................................................
# Get the proportion of employees by Education level from attrition_pop
# Proportion of employees by Education level
education_counts_pop = attrition_pop['Education'].value_counts() / len(attrition_pop)

# Print education_counts_pop
print(education_counts_pop)
