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
