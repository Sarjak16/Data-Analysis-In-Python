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

sns.relplot(kind="scatter", x= "accleration", y="mpg", data= mpg, style="origin", hue="origin")


# Show plot
plt.show()
