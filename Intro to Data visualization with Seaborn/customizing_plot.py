# Use relplot() and the mpg DataFrame to create a scatter plot with "horsepower" on the x-axis and "mpg" on the y-axis.
# Vary the size of the points by the number of cylinders in the car ("cylinders").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(kind= "scatter",x= "horsepower", y= "mpg", data= mpg, size="cylinders")



# Show plot
plt.show()


# To make this plot easier to read, use hue to vary the color of the points by the number of cylinders in the car ("cylinders").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders", hue="cylinders")

# Show plot
plt.show()

# Use relplot() and the mpg DataFrame to create a scatter plot with "acceleration" on the x-axis and "mpg" on the y-axis.
# Vary the style and color of the plot points by country of origin ("origin").
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a scatter plot of acceleration vs. mpg

sns.relplot(kind="scatter", x= "acceleration", y="mpg", data= mpg, style="origin", hue="origin")


# Show plot
plt.show()

# lineplots.............................................................................................................................................
# Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "mpg" on the y-axis.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot

sns.relplot(kind="line", x="model_year", y="mpg", data= mpg)

# Show plot
plt.show()


# Change the plot so the shaded area shows the standard deviation instead of the confidence interval for the mean.
# Make the shaded area show the standard deviation
sns.relplot(x="model_year", y="mpg",
            data=mpg, kind="line", ci="sd")

# Show plot
plt.show()

# Use relplot() and the mpg DataFrame to create a line plot with "model_year" on the x-axis and "horsepower" on the y-axis.
# Turn off the confidence intervals on the plot.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create line plot of model year vs. horsepower

sns.relplot(kind="line", x="model_year", y="horsepower", data= mpg, ci=none)


# Show plot
plt.show()

# Create different lines for each country of origin ("origin") that vary in both line style and color.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Change to create subgroups for country of origin
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin")

# Show plot
plt.show()

# Add markers for each data point to the lines.
# Use the dashes parameter to use solid lines for all countries, while still allowing for different marker styles for each line.
# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, kind="line", 
            ci=None, style="origin", 
            hue="origin", markers= True, dashes= False)

# Show plot
plt.show()
