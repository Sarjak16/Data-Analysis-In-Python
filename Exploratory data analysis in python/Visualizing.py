# Create a scatterplot showing marriage_duration on the x-axis and num_kids on the y-axis.
# Create the scatterplot
sns.scatterplot(x='marriage_duration', y='num_kids', data=divorce)
plt.show()


# Visualizing multiple variable relationships....................................................................................
# Create a pairplot to visualize the relationships between income_woman and marriage_duration in the divorce DataFrame.
# Create a pairplot for income_woman and marriage_duration
sns.pairplot(data=divorce, vars=["income_woman", "marriage_duration" ])
plt.show()
