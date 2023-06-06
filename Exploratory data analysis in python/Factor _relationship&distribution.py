# Create a scatter plot that shows woman_age_marriage on the x-axis and income_woman on the y-axis; 
# each data point should be colored based on the woman's level of education, represented by education_woman.
# Create the scatter plot
sns.scatterplot(data=divorce, x="woman_age_marriage", y="income_woman", hue="education_woman")
plt.show()
