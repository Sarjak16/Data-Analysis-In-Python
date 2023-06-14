# Exact sampling distribution.........................................................................................................
# Expand a grid representing 5 8-sided dice. That is, create a DataFrame with five columns from a dictionary, named die1 to die5. 
# The rows should contain all possibilities for throwing five dice, each numbered 1 to 8.
# Expand a grid representing 5 8-sided dice
dice = expand_grid({
    'die1':[1,2,3,4,5,6,7,8],
    'die2':[1,2,3,4,5,6,7,8],
    'die3':[1,2,3,4,5,6,7,8],
    'die4':[1,2,3,4,5,6,7,8],
    'die5':[1,2,3,4,5,6,7,8]
})


# Print the result
print(dice)

# Add a column, mean_roll, to dice, that contains the mean of the five rolls as a categorical.
# Expand a grid representing 5 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = dice[['die1', 'die2', 'die3', 'die4', 'die5']].mean(axis=1) 
                     
                    
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Print result
print(dice)

# Create a bar plot of the mean_roll categorical column, so it displays the count of each mean_roll in increasing order from 1.0 to 8.0.
# Expand a grid representing 5 8-sided dice
dice = expand_grid(
  {'die1': [1, 2, 3, 4, 5, 6, 7, 8],
   'die2': [1, 2, 3, 4, 5, 6, 7, 8],
   'die3': [1, 2, 3, 4, 5, 6, 7, 8],
   'die4': [1, 2, 3, 4, 5, 6, 7, 8],
   'die5': [1, 2, 3, 4, 5, 6, 7, 8]
  })

# Add a column of mean rolls and convert to a categorical
dice['mean_roll'] = (dice['die1'] + dice['die2'] + 
                     dice['die3'] + dice['die4'] + 
                     dice['die5']) / 5
dice['mean_roll'] = dice['mean_roll'].astype('category')

# Draw a bar plot of mean_roll
dice['mean_roll'].value_counts(sort=False).plot(kind='bar', rot=0)
plt.show()

# Generating approx sampling................................................................................
# Sample one to eight, five times, with replacement. Assign to five_rolls.
# Calculate the mean of five_rolls.
# Sample one to eight, five times, with replacement
five_rolls = np.random.choice(a=range(1, 9), size=5, replace=True)

# Print the mean of five_rolls
print(np.mean(five_rolls))

# Replicate the sampling code 1000 times, assigning each result to the list sample_means_1000.
# Replicate the sampling code 1000 times
sample_means_1000 = []
for i in range(1000):
    sample_means_1000.append(
  		np.random.choice(list(range(1, 9)), size=5, replace=True).mean()
    )
    
# Print the first 10 entries of the result
print(sample_means_1000[0:10])
