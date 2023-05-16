# Index merge for movie ratings................................................................................................................................
# To practice merging on indexes, you will merge movies and a table called ratings that holds info about movie ratings.
# Make sure your merge returns all of the rows from the movies table and not all the rows of ratings table need to be included in the result.

# The movies and ratings tables have been loaded for you.

# Merge movies and ratings on the index and save to a variable called movies_ratings, ensuring that all of the rows from the movies table are returned.

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(ratings, on='id', how='left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())
