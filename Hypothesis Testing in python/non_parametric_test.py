# Wilcoxon signed-rank test.........................................................
# Conduct a paired t-test on the percentage columns using an appropriate alternative hypothesis.
# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'], y=sample_dem_data['dem_percent_16'], paired= True,  ) 

# Print paired t-test results
print(paired_test_results)


# Conduct a Wilcoxon-signed rank test on the same columns.
# Conduct a Wilcoxon test on dem_percent_12 and dem_percent_16
wilcoxon_test_results = pingouin.wilcoxon(sample_dem_data["dem_percent_12"], sample_dem_data["dem_percent_16"])

# Print Wilcoxon test results
print(wilcoxon_test_results)



# Wilcon-mann-whitney............................................................................................
# Select weight_kilograms and late from late_shipments, assigning the name weight_vs_late.
# Convert weight_vs_late from long-to-wide format, setting columns to 'late'.
# Run a Wilcoxon-Mann-Whitney test for a difference in weight_kilograms when the shipment was late and on-time.
# Select the weight_kilograms and late columns
weight_vs_late = late_shipments[["weight_kilograms", "late"]]

# Convert weight_vs_late into wide format
weight_vs_late_wide = weight_vs_late.pivot(columns='late', 
                                           values='weight_kilograms')

# Run a two-sided Wilcoxon-Mann-Whitney test on weight_kilograms vs. late
wmw_test = pingouin.mwu(x=weight_vs_late_wide['No'],
                        y=weight_vs_late_wide['Yes'],
                        alternative='two-sided')

# Print the test results
print(wmw_test)
