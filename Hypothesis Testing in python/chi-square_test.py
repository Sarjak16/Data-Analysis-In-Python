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
