# Index merge for movie ratings................................................................................................................................
# To practice merging on indexes, you will merge movies and a table called ratings that holds info about movie ratings.
# Make sure your merge returns all of the rows from the movies table and not all the rows of ratings table need to be included in the result.

# The movies and ratings tables have been loaded for you.

# Merge movies and ratings on the index and save to a variable called movies_ratings, ensuring that all of the rows from the movies table are returned.

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())


# With the sequels table on the left, merge to it the financials table on index named id,
# ensuring that all the rows from the sequels are returned and some rows from the other table may not be returned, Save the results to sequels_fin.
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Merge the sequels_fin table to itself with an inner join,
# where the left and right tables merge on sequel and id respectively with suffixes equal to ('_org','_seq'), saving to orig_seq.
# Merge sequels and financials on index id
sequels_fin = sequels.merge(financials, on='id', how='left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', right_on='id', right_index=True, suffixes=('_org','_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']
