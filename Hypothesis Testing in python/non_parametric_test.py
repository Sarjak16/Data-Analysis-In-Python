# Wilcoxon signed-rank test.........................................................
# Conduct a paired t-test on the percentage columns using an appropriate alternative hypothesis.
# Conduct a paired t-test on dem_percent_12 and dem_percent_16
paired_test_results = pingouin.ttest(x=sample_dem_data['dem_percent_12'], y=sample_dem_data['dem_percent_16'], paired= True,  ) 

# Print paired t-test results
print(paired_test_results)
