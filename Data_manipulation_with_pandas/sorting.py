#sorting rows:........................................................................................................................
# Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind.
# Print the head of the sorted DataFrame.
#solution:
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())


# Sort homelessness by the number of homeless family_members in descending order, and save this as homelessness_fam.
# Print the head of the sorted DataFrame.
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values("family_members", ascending= False)

# Print the top few rows
print(homelessness_fam.head())


# Sort homelessness first by region (ascending), and then by number of family members (descending). Save this as homelessness_reg_fam.
# Print the head of the sorted DataFrame.

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values("region", ascending= False)

# Print the top few rows
print(homelessness_reg_fam.head())





# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region", "family_members"] ,ascending= [True, False])

# Print the top few rows
print(homelessness_reg_fam.head())


#sorting columns..........................................................................................................
# Create a DataFrame called individuals that contains only the individuals column of homelessness.
# Print the head of the result

# Select the individuals column
individuals = homelessness["individuals"]


# Print the head of the result
print(individuals.head())
