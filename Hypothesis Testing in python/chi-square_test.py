# Calculate the proportion of freight_cost_group in late_shipments grouped by vendor_inco_term.
# Propor(tion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts(normalize= True)

# Print props
print(props)


# Unstack the .value_counts() result to be in wide format instead of long.
# Proportion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts(normalize=True)

# Convert props to wide format
wide_props = props.unstack()

# Print wide_props
print(wide_props)


# Create a proportional stacked bar plot with bars filled based on freight_cost_group across the levels of vendor_inco_term.
# Proportion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts(normalize=True)

# Convert props to wide format
wide_props = props.unstack()

# Proportional stacked bar plot of freight_cost_group vs. vendor_inco_term
wide_props.plot(kind="bar", stacked= True)
plt.show()



# Perform a chi-square test of independence on freight_cost_group and vendor_inco_term in the late_shipments dataset.
# Proportion of freight_cost_group grouped by vendor_inco_term
props = late_shipments.groupby('vendor_inco_term')['freight_cost_group'].value_counts(normalize=True)

# Convert props to wide format
wide_props = props.unstack()

# Proportional stacked bar plot of freight_cost_group vs. vendor_inco_term
wide_props.plot(kind="bar", stacked=True)
plt.show()

# Determine if freight_cost_group and vendor_inco_term are independent
expected, observed, stats = pingouin.chi2_independence(data=late_shipments,x='vendor_inco_term', y='freight_cost_group', correction=False)

# Print results
print(stats[stats['test'] == 'pearson']) 


# ...................................................................................................................................................................
# chi square goodness test
# Find the total number of rows in late_shipments.
# Find the number of rows in late_shipments
n_total = len(late_shipments)

# Print n_total
print(n_total)


# Add a column named n to the hypothesized DataFrame that is the hypothesized prop column times n_total.
# Find the number of rows in late_shipments
n_total = len(late_shipments)

# Create n column that is prop column * n_total
hypothesized['n'] = hypothesized['prop'] * n_total

# Print the modified hypothesized DataFrame
print(hypothesized)

# Create a bar graph of 'n' versus 'vendor_inco_term' for the incoterm_counts data, specifying a red color.
# Find the number of rows in late_shipments
n_total = len(late_shipments)

# Create n column that is prop column * n_total
hypothesized["n"] = hypothesized["prop"] * n_total

# Plot a red bar graph of n vs. vendor_inco_term for incoterm_counts
plt.bar(incoterm_counts['vendor_inco_term'], incoterm_counts['n'], color="red", label="Observed")
plt.legend()
plt.show()
