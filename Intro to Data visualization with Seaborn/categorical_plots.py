# countplots...............................................................................................
# Use sns.catplot() to create a count plot using the survey_data DataFrame with "Internet usage" on the x-axis.
# Create count plot of internet usage
sns.catplot(kind="count", data= survey_data, x="Internet usage")


# Show plot
plt.show()

# Make the bars horizontal instead of vertical.
# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Separate this plot into two side-by-side column subplots based on "Age Category", which separates respondents into those that are younger than 21 vs. 21 and older.
# Separate into column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count", col="Age Category")

# Show plot
plt.show()

# Bar plots....................................................................................................................
# Use the survey_data DataFrame and sns.catplot() to create a bar plot with "Gender" on the x-axis and "Interested in Math" on the y-axis.
# Create a bar plot of interest in math, separated by gender
sns.catplot(kind="bar", data=survey_data, x="Gender", y="Interested in Math")


# Show plot
plt.show()

# Use sns.catplot() to create a bar plot with "study_time" on the x-axis and final grade ("G3") on the y-axis, using the student_data DataFrame.
# Create bar plot of average final grade in each study category

sns.catplot(kind="bar", x="study_time", y="G3", data= student_data)


# Show plot
plt.show()

# Using the order parameter and the category_order list that is provided, rearrange the bars so that they are in order from lowest study time to highest
# List of categories from lowest to highest
category_order = ["<2 hours", 
                  "2 to 5 hours", 
                  "5 to 10 hours", 
                  ">10 hours"]

# Rearrange the categories
sns.catplot(x="study_time", y="G3",
            data=student_data,
            kind="bar", order= category_order)

# Show plot
plt.show()
