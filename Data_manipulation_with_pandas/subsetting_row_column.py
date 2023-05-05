#subsetting rows by categorical variables...........................................................................................................

# Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic. View the printed result.

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness['region']=="South Atlantic") | (homelessness['region']=="Mid-Atlantic")]
# See the result
print(south_mid_atlantic)

# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = mojave_homelessness = homelessness[homelessness['state'].isin(canu)]
# See the result
print(mojave_homelessness)

# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
# Add another column to homelessness, named p_individuals, containing the proportion of homeless people in each state who are individuals.

# Add total col as sum of individuals and family_members
homelessness['total'] = homelessness['individuals'] + homelessness['family_members']

# Add p_individuals col as proportion of total that are individuals
homelessness['p_individuals']= homelessness['individuals'] / homelessness['total']

# See the result
print(homelessness)
