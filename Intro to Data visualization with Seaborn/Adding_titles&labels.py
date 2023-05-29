# Identify what type of object plot g is and assign it to the variable type_of_g.
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Identify plot type
type_of_g = type(g)

# Print type
print(type_of_g)


# Add the following title to this plot: "Car Weight vs. Horsepower".
# Create scatter plot
g = sns.relplot(x="weight", 
                y="horsepower", 
                data=mpg,
                kind="scatter")

# Add a title "Car Weight vs. Horsepower"

g.fig.suptitle("Car Weight vs. Horsepower")
# Show plot
plt.show()



.......................................................part2......................................................................................
# Add the following title to the plot: "Average MPG Over Time".
# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Show plot
plt.show()

# Label the x-axis as "Car Model Year" and the y-axis as "Average MPG"

# Create line plot
g = sns.lineplot(x="model_year", y="mpg_mean", 
                 data=mpg_mean,
                 hue="origin")

# Add a title "Average MPG Over Time"
g.set_title("Average MPG Over Time")

# Add x-axis and y-axis labels

g.set(xlabel="Car Model Year", ylabel="Average MPG")

# Show plot
plt.show()

# ...................................................................ROTATION.................................................................

# # Rotate the x-tick labels 90 degrees.

# Create point plot
sns.catplot(x="origin", 
            y="acceleration", 
            data=mpg, 
            kind="point", 
            join=False, 
            capsize=0.1)

# Rotate x-tick labels
plt.xticks(rotation= 90)

# Show plot
plt.show()
