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
