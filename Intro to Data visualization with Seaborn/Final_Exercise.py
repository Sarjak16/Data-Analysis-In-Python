# Set the color palette to "Blues".
# Add subgroups to color the box plots based on "Interested in Pets".
# Set the title of the FacetGrid object g to "Age of Those Interested in Pets vs. Not".
# Make the plot display using a Matplotlib function.

# Set palette to "Blues"
sns.set_palette("Blues")

# Adjust to add subgroups based on "Interested in Pets"
g = sns.catplot(x="Gender",
                y="Age", data=survey_data, 
                kind="box", hue="Interested in Pets")

# Set title to "Age of Those Interested in Pets vs. Not"
g.fig.suptitle("Age of Those Interested in Pets vs. Not")

# Show plot
plt.show()



# Set the figure style to "dark".
# Adjust the bar plot code to add subplots based on "Gender", arranged in columns.
# Add the title "Percentage of Young People Who Like Techno" to this FacetGrid plot.
# Label the x-axis "Location of Residence" and y-axis "% Who Like Techno".

# Set the figure style to "dark"
sns.set_style("dark")

# Adjust to add subplots per gender
g = sns.catplot(x="Village - town", y="Likes Techno", 
                data=survey_data, kind="bar",
                col="Gender")

# Add title and axis labels
g.fig.suptitle("Percentage of Young People Who Like Techno", y=1.02)
g.set(xlabel="Location of Residence", 
       ylabel="% Who Like Techno")

# Show plot
plt.show()
