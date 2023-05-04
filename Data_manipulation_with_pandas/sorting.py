#sorting rows:........................................................................................................................
# Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind.
# Print the head of the sorted DataFrame.
#solution:
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())
