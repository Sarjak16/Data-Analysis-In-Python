# Performing ttest()....................................................
# Conduct a t-test on the sample differences (the diff column of sample_dem_data), using an appropriate alternative hypothesis chosen from "two-sided", "less", 
# and "greater".

# Conduct a t-test on diff
test_results = pingouin.ttest(x=sample_dem_data['diff'], y=0, alternative="two-sided")
                            
# Print the test results
print(test_results)
