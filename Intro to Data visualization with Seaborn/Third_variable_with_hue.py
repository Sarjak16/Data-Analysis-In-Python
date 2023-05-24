# Hue and scatterplots.................................................................................................................
# Create a scatter plot with "absences" on the x-axis and final grade ("G3") on the y-axis using the DataFrame student_data. 
# Color the plot points based on "location" (urban vs. rural).
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of absences vs. final grade
sns.scatterplot(x="absences", y="G3", data= student_data, hue= "location")



# Show plot
plt.show()

# Make "Rural" appear before "Urban" in the plot legend.
# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()

#Hue and countplots...................................................................................................................................
# Fill in the palette_colors dictionary to map the "Rural" location value to the color "green" and the "Urban" location value to the color "blue".
# Create a count plot with "school" on the x-axis using the student_data DataFrame.
# Add subgroups to the plot using "location" variable and use the palette_colors dictionary to make the location subgroups green and blue.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# Create a count plot of school with location subgroups

sns.countplot(x="school", data=student_data, hue="location", palette=palette_colors)

# Display plot
plt.show()
