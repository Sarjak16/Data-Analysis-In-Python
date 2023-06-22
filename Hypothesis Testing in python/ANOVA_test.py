# Group late_shipments by shipment_mode and calculate the mean pack_price for each group, storing the result in xbar_pack_by_mode.
# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")["pack_price"].mean()

# Print the grouped means
print(xbar_pack_by_mode)

# Group late_shipments by shipment_mode and calculate the standard deviation pack_price for each group, storing the result in s_pack_by_mode.
# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()


# Print the grouped standard deviations
print(s_pack_by_mode)


# Create a boxplot from late_shipments with "pack_price" as x and "shipment_mode" as y.

# Calculate the mean pack_price for each shipment_mode
xbar_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].mean()

# Calculate the standard deviation of the pack_price for each shipment_mode
s_pack_by_mode = late_shipments.groupby("shipment_mode")['pack_price'].std()

# Boxplot of shipment_mode vs. pack_price
sns.boxplot(x="pack_price", y="shipment_mode", data=late_shipments)
plt.show()



#Conducting an ANOVA test..........................................................................................
#Run an ANOVA on late_shipments investigating 'pack_price' (the dependent variable) between the groups of 'shipment_mode'.
# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data=late_shipments, dv="pack_price", between="shipment_mode")



# Print anova_results
print(anova_results)



# Pairwise ttest.........................................................
# Perform pairwise t-tests on late_shipments's pack_price variable, grouped by shipment_mode, without doing any p-value adjustment.

# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pingouin.pairwise_ttests(data=late_shipments, dv="pack_price", between="shipment_mode", padjust="none") 

# Print pairwise_results
print(pairwise_results)


# Modify the pairwise t-tests to use the Bonferroni p-value adjustment.

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="bonf")

# Print pairwise_results
print(pairwise_results)
