# making scatter plot with lists.......................................................

# Import Matplotlib and Seaborn using the standard naming convention.

import matplotlib.pyplot as plt 
import seaborn as sns

# Create a scatter plot of GDP (gdp) vs. number of phones per 1000 people (phones).
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot with GDP on the x-axis and number of phones on the y-axis
sns.scatterplot(x= gdp, y= phones )

# Show plot
plt.show()

# Change the scatter plot so it displays the percent of the population that can read and write (percent_literate) on the y-axis.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change this scatter plot to have percent literate on the y-axis
sns.scatterplot(x=gdp, y=percent_literate)

# Show plot
plt.show()


# countplot.....................................................................................................
# Import Matplotlib and Seaborn using the standard naming conventions.
# Use Seaborn to create a count plot with region on the y-axis.
# Display the plot.

# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt 
import seaborn as sns


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show()




# BOX PLOTS.................................................................................................................................................
# Use sns.catplot() and the student_data DataFrame to create a box plot with "study_time" on the x-axis and "G3" on the y-axis.
# Set the ordering of the categories to study_time_order.

# Specify the category ordering
study_time_order = ["<2 hours", "2 to 5 hours", 
                    "5 to 10 hours", ">10 hours"]

# Create a box plot and set the order of the categories

sns.catplot(x="study_time", y="G3", data= student_data, kind="box", order= study_time_order)



# Show plot
plt.show()


# Use sns.catplot() to create a box plot with the student_data DataFrame, putting "internet" on the x-axis and "G3" on the y-axis.
# Add subgroups so each box plot is colored based on "location".
# Do not display the outliers.

# Create a box plot with subgroups and omit the outliers
sns.catplot(x="internet", y="G3", data= student_data, hue="location", sym="", kind="box")


# Show plot
plt.show()
