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


# subsetting rows..........................................................................................................................
# Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
#solution:
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness["individuals"] >10000]

# See the result
print(ind_gt_10k)


# 2
# Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
#solution:

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness["region"] == "Mountain"]

# See the result
print(mountain_reg)

#subsetting rows..........................................................................................................................
# Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific",
# assigning to fam_lt_1k_pac. View the printed result.
#solution:
# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac =  homelessness[(homelessness["family_members"] < 1000) & (homelessness["region"]=="Pacific")]

# See the result
print(fam_lt_1k_pac)
