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
