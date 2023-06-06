# Create a scatter plot that shows woman_age_marriage on the x-axis and income_woman on the y-axis; 
# each data point should be colored based on the woman's level of education, represented by education_woman.
# Create the scatter plot
sns.scatterplot(data=divorce, x="woman_age_marriage", y="income_woman", hue="education_woman")
plt.show()

# Create a KDE plot that shows marriage_duration on the x-axis and a different colored line for each possible number of children that a couple might have,
# represented by num_kids.
# Update the KDE plot so that marriage duration can't be smoothed too far
# Create the KDE plot
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0)
plt.show()

# Notice that the plot currently shows marriage durations less than zero; update the KDE plot so that marriage duration cannot be smoothed past the extreme data points.
# Update the KDE plot so that marriage duration can't be smoothed too far
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0)
plt.show()

# Update the code for the KDE plot from the previous step to show a cumulative distribution function for each number of children a couple has.
# Update the KDE plot to show a cumulative distribution function
sns.kdeplot(data=divorce, x="marriage_duration", hue="num_kids", cut=0, cumulative= True)
plt.show()
