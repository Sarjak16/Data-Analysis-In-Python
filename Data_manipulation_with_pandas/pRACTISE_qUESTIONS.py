# # Thechurndataset contains customers' information and whether or not they exited the company. What is the correct way to display the row labels? 
#     surname  credit_score geography  age exited
# 0  Hargrave           619    France   42    Yes
# 1      Hill           608     Spain   41     No
# 2      Onio           502    France   42    Yes
# 3      Boni           699    France   39     No
# 4  Mitchell           850     Spain   43     No

print(churn.index())

# The salesdataset contains information about daily store purchases. The filtered_salesdataset contains products that belong to Health and beautyand Sports. 

# . 
#           date       product_line     product  unit_price  quantity
# 0   2018-01-15  Health and beauty     Shampoo        6.99         7
# 3   2018-01-16             Sports    Yoga mat       39.99         5
# 5   2018-01-17  Health and beauty     Shampoo       12.99         4
# 6   2018-01-17             Sports    Yoga mat       29.99         3

filtered_sales = sales[sales["product_line"].isin(["Health and beauty", "Sports"])]
print(filtered_sales.groupby([
'product_line'
, 
'product'
])[
'unit_price'
].min())
