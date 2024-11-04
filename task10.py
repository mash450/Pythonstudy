# Given product list
prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'],  ['bread', '45kshs', '359'], 
           ['coffee', '5kshs', '79']]

# Initialize total stock
total_stock = 0

# Loop through each product to extract the stock quantity
for product in prods:
    stock = int(product[-1])  # Get the last element and convert it to an integer
    total_stock += stock  # Add the stock to the total

# Print the total stock
print("Total stock in the company:", total_stock)
