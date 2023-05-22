# Create a scatterplot of happiness_score vs. life_exp (without a trendline) using seaborn.
# Show the plot.

# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)

# Show plot
plt.show()

# Create a scatterplot of happiness_score vs. life_exp with a linear trendline using seaborn, setting ci to None.
# Show the plot.
# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()

# Calculate the correlation between life_exp and happiness_score. Save this as cor.
# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)

# Show plot
plt.show()

# Correlation between life_exp and happiness_score
cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])

print(cor)

# corelation caveats........................................................................
# Create a seaborn scatterplot (without a trendline) showing the relationship between gdp_per_cap (on the x-axis) and life_exp (on the y-axis).
# Show the plot
# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()

# Calculate the correlation between gdp_per_cap and life_exp and store as cor.
# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)

# Show plot
plt.show()
  
# Correlation between gdp_per_cap and life_exp
cor = cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])

print(cor)


# transforming variables........................................................................................
# Create a scatterplot of happiness_score versus gdp_per_cap and calculate the correlation between them.

# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x='gdp_per_cap', y='happiness_score', data=world_happiness)
plt.show()


# Calculate correlation
cor = cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)


# Add a new column to world_happiness called log_gdp_per_cap that contains the log of gdp_per_cap.
# Create a seaborn scatterplot of happiness_score versus log_gdp_per_cap.
# Calculate the correlation between log_gdp_per_cap and happiness_scor

# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of happiness_score vs. log_gdp_per_cap
sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)

plt.show()

# Calculate correlation
cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])
print(cor)
