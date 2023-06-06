# Create a scatter plot that shows woman_age_marriage on the x-axis and income_woman on the y-axis; 
# each data point should be colored based on the woman's level of education, represented by education_woman.
# Create the scatter plot
sns.scatterplot(data=divorce, x="woman_age_marriage", y="income_woman", hue="education_woman")
plt.show()

# Create a KDE plot that shows marriage_duration on the x-axis and a different colored line for each possible number of children that a couple might have,
# represented by num_kids.
# Update the KDE plot so that marriage duration can't be smoothed too far
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", ____)
plt.show()
